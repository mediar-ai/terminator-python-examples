#!/usr/bin/env python3
"""
Direct Tool Testing - Test terminator SDK tools directly without agent
"""

import asyncio
import sys
from ai_artist_agent import PaintOpenTool, PaintBrushTool, PaintDrawTool, PaintShapeTool, PaintTextTool

async def test_tools_directly():
    """Test each tool directly to see if terminator SDK actually works"""
    print("🔧 TESTING TERMINATOR SDK TOOLS DIRECTLY")
    print("="*60)
    
    try:
        # Test 1: Open Paint
        print("1. Testing PaintOpenTool...")
        open_tool = PaintOpenTool()
        result1 = open_tool._run("")
        print(f"   Result: {result1}")
        await asyncio.sleep(3)
        
        # Test 2: Use Brush
        print("\n2. Testing PaintBrushTool...")
        brush_tool = PaintBrushTool()
        result2 = brush_tool._run("size:medium, color:red")
        print(f"   Result: {result2}")
        await asyncio.sleep(2)
        
        # Test 3: Draw Something
        print("\n3. Testing PaintDrawTool...")
        draw_tool = PaintDrawTool()
        result3 = draw_tool._run("pattern:circle")
        print(f"   Result: {result3}")
        await asyncio.sleep(2)
        
        # Test 4: Add Shape
        print("\n4. Testing PaintShapeTool...")
        shape_tool = PaintShapeTool()
        result4 = shape_tool._run("shape:rectangle")
        print(f"   Result: {result4}")
        await asyncio.sleep(2)
        
        # Test 5: Add Text
        print("\n5. Testing PaintTextTool...")
        text_tool = PaintTextTool()
        result5 = text_tool._run("text:HELLO WORLD!")
        print(f"   Result: {result5}")
        
        print("\n" + "="*60)
        print("🎯 DIRECT TOOL TESTING COMPLETE!")
        print("Check MS Paint to see if anything actually happened!")
        
    except Exception as e:
        print(f"💥 ERROR: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_tools_directly()) 