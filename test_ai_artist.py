#!/usr/bin/env python3
"""
AI Artist Agent CLI Tester - Test different artistic scenarios from command line
Usage: python test_ai_artist.py [theme]

Examples:
  python test_ai_artist.py "cosmic space art"
  python test_ai_artist.py "geometric abstract"
  python test_ai_artist.py "simple circle and square"
"""

import asyncio
import sys
from ai_artist_agent import AIArtistAgent

async def test_artist_with_theme(theme):
    """Test the AI artist with a specific theme"""
    print(f"🎨 TESTING AI ARTIST AGENT")
    print("="*60)
    print(f"Theme: {theme}")
    print("="*60)
    
    try:
        artist = AIArtistAgent()
        result = await artist.create_artwork(theme)
        
        if result:
            print(f"\n✅ TEST COMPLETED SUCCESSFULLY!")
            print(f"Result: {result.get('output', 'Art created!')}")
        else:
            print(f"\n❌ TEST FAILED!")
            
    except Exception as e:
        print(f"\n💥 ERROR DURING TEST: {str(e)}")

async def main():
    """Main CLI function"""
    
    # Default themes for quick testing
    quick_themes = {
        "1": "simple red circle",
        "2": "blue square and triangle", 
        "3": "colorful geometric patterns",
        "4": "spiral and dots",
        "5": "abstract lines and shapes",
        "6": "cosmic space art",
        "7": "nature landscape", 
        "8": "digital portrait"
    }
    
    if len(sys.argv) > 1:
        # Use command line argument
        theme = " ".join(sys.argv[1:])
        print(f"🎯 Using CLI theme: {theme}")
        await test_artist_with_theme(theme)
    else:
        # Interactive quick test menu
        print("🎨 AI ARTIST AGENT - QUICK TESTER")
        print("="*50)
        print("Quick test themes:")
        for key, value in quick_themes.items():
            print(f"{key}. {value}")
        print("9. Custom theme")
        print("0. Exit")
        
        choice = input("\n🎯 Choose (0-9): ").strip()
        
        if choice == "0":
            print("👋 Goodbye!")
            return
        elif choice == "9":
            theme = input("🎨 Enter custom theme: ").strip()
            if not theme:
                theme = "abstract art"
        elif choice in quick_themes:
            theme = quick_themes[choice]
        else:
            print("❌ Invalid choice!")
            return
            
        await test_artist_with_theme(theme)

if __name__ == "__main__":
    asyncio.run(main()) 