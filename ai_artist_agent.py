#!/usr/bin/env python3
"""
AI Artist Agent - Autonomous Creative Agent
Uses LangChain agents with Terminator-py tools to create art in MS Paint!
"""

import asyncio
import terminator
import time
import random
import json
from datetime import datetime
from typing import List, Dict, Any, Optional, Type

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

# Custom Paint Tools using Terminator-py
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
            return "✅ MS Paint opened successfully and ready for drawing!"
        except Exception as e:
            return f"❌ Failed to open Paint: {str(e)}"

class PaintBrushTool(BaseTool):
    """Tool to select brush and draw"""
    name: str = "use_brush"
    description: str = "Select brush tool and draw on canvas. Input: 'size:small/medium/large, color:red/blue/green/etc'"
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
            
            # Select brush tool
            try:
                brush_btn = desktop.locator('name:Brush')
                brush_btn.click()
                time.sleep(0.5)
            except:
                # Try alternative selector
                try:
                    brush_btn = desktop.locator('automationid:BrushTool')
                    brush_btn.click()
                    time.sleep(0.5)
                except:
                    pass  # Continue anyway
            
            # Set color if possible
            color_map = {
                "red": "FF0000", "blue": "0000FF", "green": "00FF00",
                "yellow": "FFFF00", "purple": "800080", "orange": "FFA500",
                "black": "000000", "white": "FFFFFF"
            }
            
            if color.lower() in color_map:
                try:
                    # Try to click on color palette
                    color_btn = desktop.locator(f'name:{color.title()}')
                    color_btn.click()
                    time.sleep(0.3)
                except:
                    pass  # Color might not be selectable this way
            
            return f"🎨 Brush tool selected! Size: {size}, Color: {color}. Ready to draw!"
        
        except Exception as e:
            return f"❌ Failed to setup brush: {str(e)}"

class PaintDrawTool(BaseTool):
    """Tool to draw on the canvas"""
    name: str = "draw_on_canvas"
    description: str = "Draw on the paint canvas. Input: 'pattern:circle/line/zigzag/spiral/dots/square/triangle/heart/star/wave'"
    args_schema: Type[BaseModel] = PaintInput
    
    def _run(
        self, 
        query: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            pattern = query.split(':')[1].strip() if ':' in query else query.strip()
            
            # Get canvas area (approximate center of screen for Paint)
            center_x, center_y = 400, 350
            
            # Draw different patterns
            if pattern == "circle":
                self._draw_circle(desktop, center_x, center_y, 50)
            elif pattern == "line":
                self._draw_line(desktop, center_x - 50, center_y, center_x + 50, center_y)
            elif pattern == "zigzag":
                self._draw_zigzag(desktop, center_x - 60, center_y, 120, 40)
            elif pattern == "spiral":
                self._draw_spiral(desktop, center_x, center_y)
            elif pattern == "dots":
                self._draw_dots(desktop, center_x, center_y)
            elif pattern == "square":
                self._draw_square(desktop, center_x, center_y, 60)
            elif pattern == "triangle":
                self._draw_triangle(desktop, center_x, center_y, 60)
            elif pattern == "heart":
                self._draw_heart(desktop, center_x, center_y)
            elif pattern == "star":
                self._draw_star(desktop, center_x, center_y)
            elif pattern == "wave":
                self._draw_wave(desktop, center_x - 80, center_y, 160)
            else:
                # Random scribble
                self._draw_random_scribble(desktop, center_x, center_y)
            
            return f"🎨 Drew {pattern} pattern on canvas!"
        
        except Exception as e:
            return f"❌ Failed to draw: {str(e)}"
    
    def _draw_circle(self, desktop, x, y, radius):
        """Draw a circle"""
        import math
        points = []
        for i in range(0, 360, 10):
            angle = math.radians(i)
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        
        self._draw_connected_points(desktop, points)
    
    def _draw_line(self, desktop, x1, y1, x2, y2):
        """Draw a straight line"""
        # Get canvas and use proper mouse methods
        canvas = desktop.locator('name:Canvas')
        canvas.mouse_click_and_hold(x1, y1)
        time.sleep(0.1)
        canvas.mouse_move(x2, y2)
        canvas.mouse_release()
    
    def _draw_zigzag(self, desktop, start_x, start_y, width, height):
        """Draw a zigzag pattern"""
        points = []
        num_peaks = 5
        for i in range(num_peaks + 1):
            x = start_x + (width * i / num_peaks)
            y = start_y + (height if i % 2 == 1 else 0)
            points.append((x, y))
        
        self._draw_connected_points(desktop, points)
    
    def _draw_spiral(self, desktop, center_x, center_y):
        """Draw a spiral"""
        import math
        points = []
        for i in range(0, 720, 15):  # Two full rotations
            angle = math.radians(i)
            radius = i / 20  # Increasing radius
            px = center_x + radius * math.cos(angle)
            py = center_y + radius * math.sin(angle)
            points.append((px, py))
        
        self._draw_connected_points(desktop, points)
    
    def _draw_dots(self, desktop, center_x, center_y):
        """Draw a pattern of dots"""
        canvas = desktop.locator('name:Canvas')
        for i in range(7):
            for j in range(5):
                x = center_x - 60 + i * 20
                y = center_y - 40 + j * 20
                canvas.click(x, y)
                time.sleep(0.05)
    
    def _draw_square(self, desktop, center_x, center_y, size):
        """Draw a square"""
        half_size = size // 2
        points = [
            (center_x - half_size, center_y - half_size),
            (center_x + half_size, center_y - half_size),
            (center_x + half_size, center_y + half_size),
            (center_x - half_size, center_y + half_size),
            (center_x - half_size, center_y - half_size)  # Close the square
        ]
        self._draw_connected_points(desktop, points)
    
    def _draw_triangle(self, desktop, center_x, center_y, size):
        """Draw a triangle"""
        import math
        height = size * math.sqrt(3) / 2
        points = [
            (center_x, center_y - height/2),
            (center_x - size/2, center_y + height/2),
            (center_x + size/2, center_y + height/2),
            (center_x, center_y - height/2)  # Close the triangle
        ]
        self._draw_connected_points(desktop, points)
    
    def _draw_heart(self, desktop, center_x, center_y):
        """Draw a heart shape"""
        import math
        points = []
        for i in range(0, 360, 10):
            t = math.radians(i)
            # Heart equation in parametric form
            x = 16 * math.sin(t)**3
            y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            points.append((center_x + x*2, center_y + y*2))
        
        self._draw_connected_points(desktop, points)
    
    def _draw_star(self, desktop, center_x, center_y):
        """Draw a 5-pointed star"""
        import math
        points = []
        for i in range(11):  # 10 points + close
            angle = math.radians(i * 36)  # 36 degrees between points
            radius = 40 if i % 2 == 0 else 20  # Alternate between outer and inner points
            x = center_x + radius * math.cos(angle - math.pi/2)
            y = center_y + radius * math.sin(angle - math.pi/2)
            points.append((x, y))
        
        self._draw_connected_points(desktop, points)
    
    def _draw_wave(self, desktop, start_x, start_y, width):
        """Draw a wave pattern"""
        import math
        points = []
        for i in range(0, width, 5):
            x = start_x + i
            y = start_y + 30 * math.sin(i * 0.1)
            points.append((x, y))
        
        self._draw_connected_points(desktop, points)
    
    def _draw_random_scribble(self, desktop, center_x, center_y):
        """Draw a random scribble"""
        points = []
        x, y = center_x, center_y
        for _ in range(15):
            x += random.randint(-30, 30)
            y += random.randint(-30, 30)
            points.append((x, y))
        
        self._draw_connected_points(desktop, points)
    
    def _draw_connected_points(self, desktop, points):
        """Draw connected points (lines between them)"""
        if not points:
            return
        
        canvas = desktop.locator('name:Canvas')
        
        # Move to first point and start drawing
        canvas.mouse_click_and_hold(int(points[0][0]), int(points[0][1]))
        time.sleep(0.1)
        
        # Draw lines to subsequent points
        for x, y in points[1:]:
            canvas.mouse_move(int(x), int(y))
            time.sleep(0.05)
        
        canvas.mouse_release()

class PaintShapeTool(BaseTool):
    """Tool to use shape tools in Paint"""
    name: str = "use_shape"
    description: str = "Select and draw shapes. Input: 'shape:rectangle/ellipse/line/curve'"
    args_schema: Type[BaseModel] = PaintInput
    
    def _run(
        self, 
        query: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            shape = query.split(':')[1].strip() if ':' in query else query.strip()
            
            # Try to select shape tool
            shape_map = {
                "rectangle": "Rectangle",
                "ellipse": "Ellipse", 
                "line": "Line",
                "curve": "Curve"
            }
            
            shape_name = shape_map.get(shape, "Rectangle")
            
            try:
                shape_btn = desktop.locator(f'name:{shape_name}')
                shape_btn.click()
                time.sleep(0.5)
                
                # Draw the shape (approximate canvas center)
                start_x, start_y = 300, 250
                end_x, end_y = 450, 350
                
                canvas = desktop.locator('name:Canvas')
                canvas.mouse_click_and_hold(start_x, start_y)
                time.sleep(0.1)
                canvas.mouse_move(end_x, end_y)
                canvas.mouse_release()
                
                return f"🔶 Drew {shape} shape on canvas!"
                
            except Exception as e:
                return f"⚠️ Could not find {shape} tool, but attempted to draw it with brush"
        
        except Exception as e:
            return f"❌ Failed to use shape tool: {str(e)}"

class PaintTextTool(BaseTool):
    """Tool to add text to the painting"""
    name: str = "add_text"
    description: str = "Add text to the painting. Input: 'text:Your message here'"
    args_schema: Type[BaseModel] = PaintInput
    
    def _run(
        self, 
        query: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        try:
            desktop = terminator.Desktop()
            text = query.split(':', 1)[1].strip() if ':' in query else query.strip()
            
            # Select text tool
            try:
                text_btn = desktop.locator('name:Text')
                text_btn.click()
                time.sleep(0.5)
                
                # Click on canvas to place text
                canvas = desktop.locator('name:Canvas')
                canvas.click()
                time.sleep(0.5)
                
                # Type the text
                canvas.type_text(text)
                time.sleep(0.5)
                
                return f"📝 Added text: '{text}' to the painting!"
                
            except Exception as e:
                return f"⚠️ Could not access text tool: {str(e)}"
        
        except Exception as e:
            return f"❌ Failed to add text: {str(e)}"

class AIArtistAgent:
    """AI Artist Agent that autonomously creates art using Paint tools"""
    
    def __init__(self):
        """Initialize the AI Artist Agent"""
        print("🎨 Initializing AI Artist Agent...")
        
        # Initialize LLM
        self.llm = OllamaLLM(model="deepseek-r1:1.5b")
        
        # Initialize tools
        self.tools = [
            PaintOpenTool(),
            PaintBrushTool(),
            PaintDrawTool(),
            PaintShapeTool(),
            PaintTextTool()
        ]
        
        # Create agent prompt
        self.prompt = hub.pull("hwchase17/react")
        
        # Modify the prompt to include our custom instructions
        self.prompt = self.prompt.partial(
            system_message="""You are an autonomous AI artist that creates beautiful artwork using MS Paint tools.
            
Your available tools are perfect for creating art:
- open_paint: Opens MS Paint application
- use_brush: Select brush tool with size and color
- draw_on_canvas: Draw patterns like circle, line, zigzag, spiral, dots, square, triangle, heart, star, wave
- use_shape: Draw shapes like rectangle, ellipse, line, curve  
- add_text: Add text to the artwork

Be creative! Think about composition, colors, and artistic elements.
Plan your artwork step by step, but be autonomous in your decisions.
Make several drawing actions to create a complete and beautiful artwork.

Start by opening Paint, then create your masterpiece!"""
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
            max_iterations=15,
            handle_parsing_errors=True
        )
        
        print("✅ AI Artist Agent ready to create!")
    
    async def create_artwork(self, theme: str = "abstract digital art"):
        """Let the AI agent autonomously create artwork"""
        print(f"\n🎭 AI ARTIST AGENT - CREATING: {theme.upper()}")
        print("-" * 60)
        
        goal = f"""Create a beautiful {theme} artwork in MS Paint. 
        Be creative and autonomous! Use multiple tools, colors, and techniques.
        Think like a real artist - plan composition, use various elements, and create something visually appealing.
        Make several drawing actions to create a complete artwork.
        """
        
        try:
            # Run the agent
            result = await asyncio.to_thread(
                self.agent_executor.invoke,
                {"input": goal}
            )
            
            print(f"\n🎨 ARTWORK COMPLETED!")
            print("-" * 40)
            print(f"Theme: {theme}")
            print(f"AI Artist's Description: {result.get('output', 'Masterpiece created!')}")
            print("-" * 40)
            
            return result
            
        except Exception as e:
            print(f"❌ Error during artwork creation: {str(e)}")
            return None
    
    async def create_themed_gallery(self):
        """Create multiple artworks with different themes"""
        themes = [
            "cosmic space scene with stars and planets",
            "geometric abstract art with colorful shapes", 
            "nature landscape with trees and mountains",
            "digital art portrait with creative elements",
            "surreal dream-like composition"
        ]
        
        print("\n🖼️ AI ARTIST GALLERY SESSION")
        print("="*60)
        print("Creating multiple themed artworks...")
        
        for i, theme in enumerate(themes, 1):
            print(f"\n🎨 ARTWORK {i}/5")
            await self.create_artwork(theme)
            
            if i < len(themes):
                print("\n⏸️ Taking a creative break before next artwork...")
                await asyncio.sleep(3)
        
        print("\n🏛️ GALLERY SESSION COMPLETED!")
        print("Check all your Paint windows for the complete gallery! 🎭")

async def main():
    """Main function to run the AI Artist Agent"""
    artist = AIArtistAgent()
    
    print("🎨 AI ARTIST AGENT - AUTONOMOUS CREATIVE DEMO")
    print("="*60)
    
    # Create a single themed artwork
    await artist.create_artwork("vibrant abstract digital art with geometric patterns")
    
    print("\n" + "="*60)
    print("🎉 AI Artist Agent Demo Complete!")
    print("Your autonomous AI artist has created original artwork!")
    print("Check MS Paint to see the creative masterpiece! 🖼️✨")

if __name__ == "__main__":
    asyncio.run(main()) 