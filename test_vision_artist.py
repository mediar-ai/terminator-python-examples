#!/usr/bin/env python3
"""
Test Vision Artist Agent - Command line testing with various themes
"""

import asyncio
import sys
from ai_artist_vision import AIArtistVisionAgent

async def test_vision_artist(theme=None):
    """Test the vision artist with different themes"""
    
    # Predefined themes for testing
    themes = {
        "geometric": "geometric shapes with circles, squares, and stars",
        "organic": "organic flowing patterns with hearts and spirals", 
        "minimal": "minimal composition with simple lines and dots",
        "complex": "complex layered artwork with multiple overlapping elements",
        "portrait": "abstract portrait using geometric shapes",
        "landscape": "landscape scene using basic shapes and lines",
        "mandala": "mandala pattern with symmetrical design",
        "abstract": "abstract expressionist composition"
    }
    
    if theme:
        if theme in themes:
            description = themes[theme]
            print(f"🎨 Testing theme: {theme} - {description}")
        else:
            description = theme
            print(f"🎨 Testing custom theme: {theme}")
    else:
        # Interactive selection
        print("🎨👁️ VISION AI ARTIST - THEME SELECTOR")
        print("="*50)
        print("Available themes:")
        for i, (key, desc) in enumerate(themes.items(), 1):
            print(f"  {i}. {key}: {desc}")
        print(f"  {len(themes)+1}. custom: Enter your own theme")
        
        try:
            choice = input(f"\nSelect theme (1-{len(themes)+1}): ").strip()
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(themes):
                    theme_key = list(themes.keys())[choice_num - 1]
                    description = themes[theme_key]
                    print(f"\n🎯 Selected: {theme_key}")
                elif choice_num == len(themes) + 1:
                    description = input("Enter your custom theme: ").strip()
                    print(f"\n🎯 Custom theme: {description}")
                else:
                    description = "geometric shapes with colorful patterns"
                    print(f"\n🎯 Default: {description}")
            else:
                description = "geometric shapes with colorful patterns"
                print(f"\n🎯 Default: {description}")
        except:
            description = "geometric shapes with colorful patterns" 
            print(f"\n🎯 Default: {description}")
    
    # Create and run the vision artist
    print("\n" + "="*70)
    artist = AIArtistVisionAgent()
    await artist.create_verified_artwork(description)

async def test_direct_capture():
    """Test the capture functionality directly"""
    print("📸 TESTING DIRECT CAPTURE FUNCTIONALITY")
    print("-" * 50)
    
    from ai_artist_vision import CaptureCanvasTool, AnalyzeArtworkTool
    
    # Test capture
    capture_tool = CaptureCanvasTool()
    print("1. Testing canvas capture...")
    result = capture_tool._run("test capture")
    print(f"   Result: {result}")
    
    # Test analysis
    analyze_tool = AnalyzeArtworkTool()
    print("2. Testing artwork analysis...")
    result = analyze_tool._run("analyze the captured image")
    print(f"   Result: {result}")

def main():
    """Main CLI function"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "capture":
            # Test capture functionality
            asyncio.run(test_direct_capture())
        else:
            # Use provided theme
            theme = " ".join(sys.argv[1:])
            asyncio.run(test_vision_artist(theme))
    else:
        # Interactive mode
        asyncio.run(test_vision_artist())

if __name__ == "__main__":
    main() 