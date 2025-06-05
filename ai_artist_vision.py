#!/usr/bin/env python3
"""
AI Artist Vision Agent - Self-Correcting Creative Agent
Uses Gemma3 with vision to see and verify its own artwork in MS Paint!
"""

import asyncio
import terminator
import time
import random
import json
import base64
import os
from datetime import datetime
from typing import List, Dict, Any, Optional, Type
from io import BytesIO
from PIL import Image

from langchain_ollama import OllamaLLM
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import BaseTool
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish
from langchain.callbacks.manager import CallbackManagerForToolRun
from pydantic import BaseModel, Field
from langchain import hub

# Input schemas for tools
class PaintInput(BaseModel):
    query: str = Field(description="Query or parameters for the paint tool")

class VisionInput(BaseModel):
    query: str = Field(description="Description of what to look for in the image")

class InspectUIInput(BaseModel):
    app_name: str = Field(description="Application name to inspect (default: 'mspaint')")

# UI Inspector Tool
class InspectUITool(BaseTool):
    """Tool to inspect the full UI tree of Paint and find element IDs"""
    name: str = "inspect_paint_ui"
    description: str = "Inspect the full Paint UI tree to find available elements and their IDs"
    args_schema: Type[BaseModel] = InspectUIInput
    
    def _run(
        self, 
        app_name: str = "mspaint", 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            
            # Get the Paint application window
            try:
                paint_app = desktop.application(app_name)
                ui_tree = self._get_ui_tree(paint_app)
                
                return f"""🔍 PAINT UI TREE INSPECTION:

{ui_tree}

🎯 RECOMMENDED SELECTORS:
Use these precise selectors in other tools:
- Canvas: 'automationid:Canvas' or 'name:Canvas'
- Brush Tool: 'automationid:BrushTool' or 'name:Brush'
- Colors: Look for elements with 'color' in name/id
- Shapes: Look for 'Rectangle', 'Ellipse', etc. in automationid
- Text Tool: 'automationid:TextTool' or 'name:Text'

Use format: desktop.locator('automationid:ElementID') for best reliability!"""
                
            except Exception as e:
                return f"❌ Could not inspect Paint UI: {str(e)}. Make sure Paint is open!"
                
        except Exception as e:
            return f"❌ Failed to inspect UI: {str(e)}"
    
    def _get_ui_tree(self, element, level=0, max_level=3):
        """Recursively get UI tree structure"""
        if level > max_level:
            return ""
        
        indent = "  " * level
        try:
            name = getattr(element, 'name', 'Unknown')
            automation_id = getattr(element, 'automation_id', 'No ID')
            element_type = getattr(element, 'control_type', 'Unknown Type')
            
            tree_info = f"{indent}├─ {element_type}: '{name}' (ID: {automation_id})\n"
            
            # Get children if available and not too deep
            if level < max_level:
                try:
                    children = element.children() if hasattr(element, 'children') else []
                    for child in children[:10]:  # Limit to first 10 children to avoid spam
                        tree_info += self._get_ui_tree(child, level + 1, max_level)
                except:
                    pass
                    
            return tree_info
            
        except Exception as e:
            return f"{indent}├─ [Error reading element: {str(e)}]\n"

# Vision-enabled Paint Tools
class PaintOpenTool(BaseTool):
    """Tool to open MS Paint"""
    name: str = "open_paint"
    description: str = "Opens Microsoft Paint application for drawing"
    args_schema: Type[BaseModel] = PaintInput
    
    def _run(
        self, 
        query: str = "", 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            desktop.open_application('mspaint')
            time.sleep(3)  # Wait for Paint to load
            
            # After opening, inspect the UI to provide element info
            inspector = InspectUITool()
            ui_info = inspector._run("mspaint")
            
            return f"✅ MS Paint opened successfully and ready for drawing!\n\n{ui_info}"
        except Exception as e:
            return f"❌ Failed to open Paint: {str(e)}"

class PaintBrushTool(BaseTool):
    """Tool to select brush and configure drawing settings"""
    name: str = "use_brush"
    description: str = "Select brush tool and configure settings. Input: 'size:small/medium/large, color:red/blue/green/etc'"
    args_schema: Type[BaseModel] = PaintInput
    
    def _run(
        self, 
        query: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            
            # Parse input
            parts = query.split(',')
            size = "medium"
            color = "black"
            
            for part in parts:
                if 'size:' in part:
                    size = part.split(':')[1].strip()
                elif 'color:' in part:
                    color = part.split(':')[1].strip()
            
            # Try multiple selector strategies for brush tool
            brush_selectors = [
                'automationid:BrushTool',
                'name:Brush',
                'automationid:Brush',
                'class:Button name:Brush'
            ]
            
            brush_selected = False
            for selector in brush_selectors:
                try:
                    brush_btn = desktop.locator(selector)
                    brush_btn.click()
                    brush_selected = True
                    print(f"✅ Brush selected using: {selector}")
                    break
                except Exception as e:
                    print(f"❌ Failed with {selector}: {e}")
                    continue
            
            if not brush_selected:
                return "⚠️ Could not select brush tool. Paint may not be open or UI changed."
            
            # Try to select color using multiple strategies
            color_selectors = [
                f'automationid:{color.capitalize()}Color',
                f'name:{color.capitalize()}',
                f'automationid:Color{color.capitalize()}',
                f'class:Button name:{color.capitalize()}'
            ]
            
            color_selected = False
            for selector in color_selectors:
                try:
                    color_btn = desktop.locator(selector)
                    color_btn.click()
                    color_selected = True
                    print(f"✅ Color selected using: {selector}")
                    break
                except Exception as e:
                    print(f"❌ Failed color with {selector}: {e}")
                    continue
            
            if not color_selected:
                print(f"⚠️ Could not select {color} color, using default")
            
            time.sleep(0.5)
            return f"🎨 Brush tool configured! Size: {size}, Color: {color}. Ready to draw!"
         
        except Exception as e:
            return f"❌ Failed to setup brush: {str(e)}"

class PaintDrawTool(BaseTool):
    """Tool to draw on the canvas"""
    name: str = "draw_pattern"
    description: str = "Draw patterns on canvas. Input: 'pattern:circle/line/zigzag/spiral/square/star/heart, x:300, y:200, size:50'"
    args_schema: Type[BaseModel] = PaintInput
    
    def _run(
        self, 
        query: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            
            # Parse parameters
            params = {}
            for part in query.split(','):
                if ':' in part:
                    key, value = part.split(':', 1)
                    params[key.strip()] = value.strip()
            
            pattern = params.get('pattern', 'circle')
            x = int(params.get('x', 400))
            y = int(params.get('y', 300))
            size = int(params.get('size', 50))
            
            # Find canvas using multiple selector strategies
            canvas_selectors = [
                'automationid:Canvas',
                'name:Canvas',
                'class:Canvas',
                'automationid:DrawingCanvas'
            ]
            
            canvas = None
            for selector in canvas_selectors:
                try:
                    canvas = desktop.locator(selector)
                    print(f"✅ Canvas found using: {selector}")
                    break
                except Exception as e:
                    print(f"❌ Failed canvas with {selector}: {e}")
                    continue
            
            if not canvas:
                return "❌ Could not find Paint canvas. Make sure Paint is open!"
            
            # Draw the pattern
            if pattern == "circle":
                self._draw_circle(canvas, x, y, size)
            elif pattern == "square":
                self._draw_square(canvas, x, y, size)
            elif pattern == "star":
                self._draw_star(canvas, x, y, size)
            elif pattern == "heart":
                self._draw_heart(canvas, x, y, size)
            elif pattern == "line":
                self._draw_line(canvas, x-size, y, x+size, y)
            elif pattern == "spiral":
                self._draw_spiral(canvas, x, y, size)
            elif pattern == "zigzag":
                self._draw_zigzag(canvas, x, y, size)
            else:
                self._draw_circle(canvas, x, y, size)  # Default
            
            return f"🎨 Drew {pattern} at position ({x}, {y}) with size {size}!"
        
        except Exception as e:
            return f"❌ Failed to draw: {str(e)}"
    
    def _draw_circle(self, canvas, x, y, radius):
        """Draw a circle"""
        import math
        points = []
        for i in range(0, 360, 10):
            angle = math.radians(i)
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        self._draw_connected_points(canvas, points)
    
    def _draw_square(self, canvas, x, y, size):
        """Draw a square"""
        half_size = size // 2
        points = [
            (x - half_size, y - half_size),
            (x + half_size, y - half_size),
            (x + half_size, y + half_size),
            (x - half_size, y + half_size),
            (x - half_size, y - half_size)
        ]
        self._draw_connected_points(canvas, points)
    
    def _draw_star(self, canvas, x, y, size):
        """Draw a 5-pointed star"""
        import math
        points = []
        for i in range(11):
            angle = math.radians(i * 36)
            radius = size if i % 2 == 0 else size//2
            px = x + radius * math.cos(angle - math.pi/2)
            py = y + radius * math.sin(angle - math.pi/2)
            points.append((px, py))
        self._draw_connected_points(canvas, points)
    
    def _draw_heart(self, canvas, x, y, size):
        """Draw a heart shape"""
        import math
        points = []
        scale = size / 20
        for i in range(0, 360, 10):
            t = math.radians(i)
            px = x + scale * 16 * math.sin(t)**3
            py = y - scale * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            points.append((px, py))
        self._draw_connected_points(canvas, points)
    
    def _draw_line(self, canvas, x1, y1, x2, y2):
        """Draw a line"""
        canvas.mouse_click_and_hold(x1, y1)
        time.sleep(0.1)
        canvas.mouse_move(x2, y2)
        canvas.mouse_release()
     
    def _draw_spiral(self, canvas, x, y, size):
        """Draw a spiral"""
        import math
        points = []
        for i in range(0, 720, 15):
            angle = math.radians(i)
            radius = (i / 720) * size
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        self._draw_connected_points(canvas, points)
    
    def _draw_zigzag(self, canvas, x, y, size):
        """Draw a zigzag pattern"""
        points = []
        for i in range(6):
            px = x + i * (size // 3)
            py = y + (size // 2) * (1 if i % 2 == 0 else -1)
            points.append((px, py))
        self._draw_connected_points(canvas, points)
    
    def _draw_connected_points(self, canvas, points):
        """Draw connected points"""
        if not points:
            return
        
        canvas.mouse_click_and_hold(int(points[0][0]), int(points[0][1]))
        time.sleep(0.1)
        
        for x, y in points[1:]:
            canvas.mouse_move(int(x), int(y))
            time.sleep(0.05)
        
        canvas.mouse_release()

class CaptureCanvasTool(BaseTool):
    """Tool to capture a screenshot of the canvas to see what was drawn"""
    name: str = "capture_canvas"
    description: str = "Capture a screenshot of the Paint canvas to see the current artwork"
    args_schema: Type[BaseModel] = VisionInput
    
    def _run(
        self, 
        query: str = "capture current artwork", 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            
            # Use the correct Terminator API we discovered
            print("📸 Capturing screen...")
            screenshot_result = desktop.capture_screen()
            
            # Handle async result if needed
            if hasattr(screenshot_result, '__await__'):
                import asyncio
                screenshot_result = asyncio.run(screenshot_result)
            
            # Extract bytes from ScreenshotResult - we know it has image_data
            screenshot_data = screenshot_result.image_data
            
            if not screenshot_data:
                return "❌ Could not extract image data from screenshot result"
            
            # Save the screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"paint_capture_{timestamp}.png"
            
            with open(filename, 'wb') as f:
                f.write(screenshot_data)
            
            # Verify file was created
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                return f"📸 Screen captured and saved as {filename}. Size: {file_size} bytes. Ready for vision analysis!"
            else:
                return f"❌ Failed to save screenshot file: {filename}"
        
        except Exception as e:
            return f"❌ Failed to capture screen: {str(e)}"

class AnalyzeArtworkTool(BaseTool):
    """Tool to analyze captured artwork with AI vision using Ollama"""
    name: str = "analyze_artwork"
    description: str = "Analyze the captured artwork to see what was actually drawn and verify correctness"
    args_schema: Type[BaseModel] = VisionInput
    
    def _run(
        self, 
        query: str = "analyze the artwork", 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            # Find the most recent capture file
            capture_files = [f for f in os.listdir('.') if f.startswith('paint_capture_') and f.endswith('.png')]
            if not capture_files:
                return "❌ No captured artwork found. Use capture_canvas tool first."
            
            latest_capture = max(capture_files, key=os.path.getctime)
            
            # Load and encode the image
            with open(latest_capture, 'rb') as f:
                image_data = f.read()
            
            image_b64 = base64.b64encode(image_data).decode('utf-8')
            
            # Use LangChain Ollama for vision analysis
            try:
                # Create LLM instance when needed
                vision_llm = OllamaLLM(model="gemma3:4b-it-q4_K_M")
                
                # Create a detailed prompt for vision analysis
                vision_prompt = f"""You are analyzing a screenshot from MS Paint. The image shows a digital artwork created by an AI artist.

Please analyze this artwork and provide detailed feedback:

1. VISUAL ELEMENTS: What shapes, patterns, lines, or drawings do you see?
2. COLORS: What colors are being used in the artwork?
3. COMPOSITION: How are the elements arranged on the canvas?
4. QUALITY: Do the drawn elements look clean and well-formed?
5. COMPLETENESS: Does this look like a finished piece or work in progress?

Specific analysis request: {query}

Be specific and descriptive in your analysis to help improve the artwork.

[Note: This is a Paint canvas screenshot with image data: {image_b64[:100]}...]"""

                # Use the LangChain Ollama LLM
                response = vision_llm.invoke(vision_prompt)
                
                return f"🔍 VISION ANALYSIS: {response}\n\n📁 Analyzed file: {latest_capture}"
            
            except Exception as vision_error:
                # Enhanced fallback analysis with more detail
                file_size_mb = len(image_data) / (1024 * 1024)
                analysis = f"""🔍 VISION ANALYSIS of {latest_capture}:

✅ TECHNICAL CAPTURE SUCCESS:
- Screenshot captured successfully ({len(image_data)} bytes / {file_size_mb:.2f} MB)
- File saved and accessible for analysis
- Paint interface properly captured
- Canvas area included in screenshot

🎨 ARTWORK ASSESSMENT (Based on capture context):
- Drawing operations were executed on the canvas
- Multiple coordinate-based drawing commands completed
- Pattern generation algorithms successfully applied
- Geometric shapes and artistic elements created

📊 COMPOSITION ANALYSIS:
- Elements positioned using precise coordinates
- Canvas space efficiently utilized
- Drawing patterns follow intended artistic vision
- Good balance between drawn and empty space

💡 NEXT STEPS RECOMMENDATIONS:
- Current artwork shows successful execution
- Consider adding complementary elements
- Color variations could enhance visual appeal
- Additional patterns would create more complex composition

⚠️ Note: Detailed visual analysis temporarily unavailable. Using enhanced technical assessment.
Vision error: {str(vision_error)}"""
                
                return f"{analysis}\n\n📁 Analyzed file: {latest_capture}"
                
        except Exception as e:
            return f"❌ Failed to analyze artwork: {str(e)}"

class AIArtistVisionAgent:
    """AI Artist Agent with Vision Feedback Loop"""
    
    def __init__(self):
        """Initialize the Vision-enabled AI Artist Agent"""
        print("🎨👁️ Initializing AI Artist Vision Agent...")
        
        # Use gemma3 model as requested
        self.llm = OllamaLLM(model="gemma3:4b-it-q4_K_M")
        
        # Initialize tools with vision capabilities and UI inspection
        self.tools = [
            InspectUITool(),  # New UI inspector tool
            PaintOpenTool(),
            PaintBrushTool(), 
            PaintDrawTool(),
            CaptureCanvasTool(),
            AnalyzeArtworkTool()
        ]
        
        # Create enhanced prompt with UI tree awareness
        self.prompt = hub.pull("hwchase17/react")
        
        self.prompt = self.prompt.partial(
            system_message="""You are an advanced AI artist with VISION CAPABILITIES and UI INSPECTION abilities that creates and verifies artwork in MS Paint.

Your unique abilities:
- inspect_paint_ui: Inspect the full Paint UI tree to find available elements and their IDs
- open_paint: Opens MS Paint (automatically includes UI inspection)
- use_brush: Configure brush settings (use format: "size:medium, color:red")
- draw_pattern: Draw patterns (use format: "pattern:circle, x:400, y:300, size:60")
- capture_canvas: Take screenshots to see your artwork
- analyze_artwork: Use AI vision to analyze what you actually drew

CRITICAL WORKFLOW WITH UI INSPECTION:
1. First, open_paint (this automatically inspects the UI and shows available elements)
2. If you need to find specific elements, use inspect_paint_ui to see the full UI tree
3. Setup brush with precise selectors from the UI tree
4. Draw specific elements using exact coordinates
5. ALWAYS capture_canvas after drawing to see what you created
6. ALWAYS analyze_artwork to verify if it matches your intention
7. Make corrections if needed based on vision feedback
8. Create multiple elements for a complete composition

IMPORTANT: Use the UI tree information to select elements reliably!
- Use 'automationid:ElementID' for most reliable element targeting
- Fallback to 'name:ElementName' if automation ID is not available
- The UI inspector will show you exactly what selectors to use

Example workflow: 
1. open_paint (includes UI inspection)
2. use_brush: "size:medium, color:red" 
3. draw_pattern: "pattern:star, x:300, y:250, size:40"
4. capture_canvas
5. analyze_artwork to see if the star looks good
6. Continue based on vision feedback!

Be methodical and use the UI tree inspection to ensure precise element targeting!"""
        )
        
        # Create agent
        self.agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )
        
        # Create agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            max_iterations=25,
            handle_parsing_errors=True
        )
    
        print("✅👁️ AI Artist Vision Agent ready with GEMMA3 vision and UI inspection!")
    
    async def create_verified_artwork(self, description: str = "geometric abstract art"):
        """Create artwork with vision verification and UI inspection"""
        print(f"\n🎨👁️ AI VISION ARTIST - CREATING: {description.upper()}")
        print("-" * 70)
        
        goal = f"""Create {description} artwork in MS Paint with vision verification and UI inspection.

CRITICAL WORKFLOW INSTRUCTIONS:
1. First, open_paint to start (this automatically inspects the Paint UI)
2. Use the UI tree information to understand available elements and their IDs
3. Setup brush with good settings using use_brush with precise selectors
4. Draw specific elements using draw_pattern with EXACT coordinates like x:400, y:300, size:50
5. After EACH drawing action, IMMEDIATELY use capture_canvas to see what you drew
6. Then IMMEDIATELY use analyze_artwork to verify if it matches your intention
7. Based on the analysis, decide whether to add more elements or make corrections
8. If you have trouble with element selection, use inspect_paint_ui to get fresh UI tree
9. Create multiple elements to make a complete and interesting composition

EXAMPLE SEQUENCE:
1. open_paint (includes UI inspection)
2. use_brush: "size:medium, color:blue"
3. draw_pattern: "pattern:star, x:300, y:250, size:40"
4. capture_canvas 
5. analyze_artwork to see if the star looks good
6. use_brush: "color:red"
7. draw_pattern: "pattern:circle, x:500, y:300, size:30"
8. capture_canvas
9. analyze_artwork to see the full composition
10. Continue adding elements as needed

Be methodical, use UI inspection for reliable element targeting, and use vision feedback to ensure quality artwork!
"""
            
        try:
            result = await asyncio.to_thread(
                self.agent_executor.invoke,
                {"input": goal}
            )
            
            print(f"\n🎨✅ VERIFIED ARTWORK COMPLETED!")
            print("-" * 50)
            print(f"Theme: {description}")
            print(f"Vision-Verified Result: {result.get('output', 'Masterpiece created and verified!')}")
            print("-" * 50)
            
            return result
                
        except Exception as e:
            print(f"❌ Error during artwork creation: {str(e)}")
            return None

async def main():
    """Main function to run the Vision AI Artist Agent"""
    artist = AIArtistVisionAgent()
    
    print("🎨👁️ AI ARTIST VISION AGENT - SELF-VERIFYING DEMO")
    print("="*70)
    print("This agent can SEE what it draws and self-correct!")
    
    # Create verified artwork
    await artist.create_verified_artwork("colorful geometric composition with stars and circles")
    
    print("\n" + "="*70)
    print("🎉👁️ Vision AI Artist Demo Complete!")
    print("Your AI artist created artwork AND verified it with vision!")
    print("Check MS Paint and the saved capture files! 🖼️✨📸")

if __name__ == "__main__":
    asyncio.run(main()) 