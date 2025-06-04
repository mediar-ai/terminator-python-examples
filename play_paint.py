#!/usr/bin/env python3
"""
Paint automation - Let's have some fun drawing!
Automates Windows Paint to create drawings
"""

import asyncio
import terminator

async def open_paint():
    """Open MS Paint"""
    desktop = terminator.Desktop()
    print("🎨 Opening Paint...")
    desktop.open_application('mspaint')
    await asyncio.sleep(3)
    return desktop

async def select_brush_tool(desktop):
    """Select the brush tool"""
    try:
        # Try to find and click the brush tool
        brush = desktop.locator('name:Brush')
        brush.click()
        print("✓ Brush tool selected")
        await asyncio.sleep(0.5)
        return True
    except Exception as e:
        print(f"⚠ Could not find brush tool: {e}")
        return False

async def select_color(desktop, color_name):
    """Select a color from the palette"""
    try:
        color = desktop.locator(f'name:{color_name}')
        color.click()
        print(f"✓ {color_name} color selected")
        await asyncio.sleep(0.3)
        return True
    except Exception as e:
        print(f"⚠ Could not select {color_name}: {e}")
        return False

async def draw_simple_pattern(desktop):
    """Draw a simple pattern by clicking around the canvas"""
    try:
        # Find the canvas area (this might need adjustment based on Paint version)
        canvas = desktop.locator('name:Canvas') 
        
        # If canvas not found, try alternative names
        if not canvas.is_visible():
            canvas = desktop.locator('window:Paint')
        
        print("🖌️ Drawing pattern...")
        
        # Click multiple points to create a pattern
        for i in range(5):
            canvas.click()
            await asyncio.sleep(0.2)
        
        print("✓ Pattern drawn!")
        return True
        
    except Exception as e:
        print(f"⚠ Could not draw pattern: {e}")
        return False

async def use_text_tool(desktop):
    """Use the text tool to write something"""
    try:
        # Select text tool
        text_tool = desktop.locator('name:Text')
        text_tool.click()
        print("✓ Text tool selected")
        await asyncio.sleep(0.5)
        
        # Click on canvas to place text
        canvas = desktop.locator('window:Paint')
        canvas.click()
        await asyncio.sleep(0.5)
        
        # Type text (this should create a text box)
        desktop.type_text("Hello from Terminator SDK! 🤖")
        print("✓ Text written")
        
        return True
        
    except Exception as e:
        print(f"⚠ Could not use text tool: {e}")
        return False

async def try_shapes(desktop):
    """Try to use shape tools"""
    try:
        shapes = ['Rectangle', 'Circle', 'Line']
        
        for shape in shapes:
            try:
                shape_tool = desktop.locator(f'name:{shape}')
                shape_tool.click()
                print(f"✓ {shape} tool selected")
                await asyncio.sleep(0.5)
                
                # Click and drag to create shape (simplified)
                canvas = desktop.locator('window:Paint')
                canvas.click()
                await asyncio.sleep(0.3)
                
            except Exception as e:
                print(f"⚠ Could not use {shape} tool: {e}")
        
        return True
        
    except Exception as e:
        print(f"⚠ Shape tools failed: {e}")
        return False

async def paint_demo():
    """Main paint demonstration"""
    print("=== Paint Automation Demo ===\n")
    
    try:
        desktop = await open_paint()
        
        # Try different paint operations
        await select_brush_tool(desktop)
        await select_color(desktop, 'Red')
        await draw_simple_pattern(desktop)
        
        await asyncio.sleep(1)
        
        await select_color(desktop, 'Blue') 
        await draw_simple_pattern(desktop)
        
        await asyncio.sleep(1)
        
        await use_text_tool(desktop)
        
        await asyncio.sleep(1)
        
        await try_shapes(desktop)
        
        print("\n🎨 Paint demo completed!")
        print("Check your Paint window for the artwork!")
        
    except Exception as e:
        print(f"❌ Paint demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(paint_demo()) 