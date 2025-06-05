#!/usr/bin/env python3
"""
AI Artist Agent Runner - Easy interface to run different artistic demos
"""

import asyncio
from ai_artist_agent import AIArtistAgent

async def main():
    """Main menu for AI Artist Agent demos"""
    print("🎨 AI ARTIST AGENT - AUTONOMOUS CREATIVE SYSTEM")
    print("="*60)
    print("Powered by LangChain + DeepSeek-R1 + Terminator-py")
    print("="*60)
    
    while True:
        print("\n🎭 Choose your artistic adventure:")
        print("1. 🌌 Cosmic Space Art")
        print("2. 🔷 Geometric Abstract")
        print("3. 🌲 Nature Landscape") 
        print("4. 🎨 Digital Portrait")
        print("5. 🌀 Surreal Dreams")
        print("6. 🎲 Surprise Me! (Random)")
        print("7. 🖼️ Full Gallery (5 artworks)")
        print("8. 🛠️ Custom Theme")
        print("9. ❌ Exit")
        
        choice = input("\n🎯 Enter your choice (1-9): ").strip()
        
        if choice == "1":
            theme = "cosmic space scene with stars, planets, and nebulae"
        elif choice == "2":
            theme = "geometric abstract art with colorful shapes and patterns"
        elif choice == "3":
            theme = "nature landscape with trees, mountains, and flowing water"
        elif choice == "4":
            theme = "digital art portrait with creative elements and vibrant colors"
        elif choice == "5":
            theme = "surreal dream-like composition with impossible geometry"
        elif choice == "6":
            import random
            themes = [
                "underwater scene with fish and coral",
                "steampunk mechanical contraption",
                "magical forest with glowing elements", 
                "cyberpunk cityscape with neon lights",
                "mandala pattern with intricate designs",
                "musical instruments and notes floating",
                "vintage robot in retro style",
                "butterfly garden with colorful flowers"
            ]
            theme = random.choice(themes)
            print(f"🎲 Surprise theme: {theme}")
        elif choice == "7":
            artist = AIArtistAgent()
            await artist.create_themed_gallery()
            continue
        elif choice == "8":
            theme = input("🎨 Enter your custom theme: ").strip()
            if not theme:
                theme = "creative abstract art"
        elif choice == "9":
            print("🎨 Thanks for using AI Artist Agent! Keep creating! ✨")
            break
        else:
            print("❌ Invalid choice. Please try again.")
            continue
        
        if choice in ["1", "2", "3", "4", "5", "6", "8"]:
            print(f"\n🎨 Creating artwork: {theme}")
            print("-" * 50)
            
            artist = AIArtistAgent()
            await artist.create_artwork(theme)
            
            print("\n🎉 Artwork completed! Check MS Paint! 🖼️")
            
            continue_choice = input("\n🔄 Create another artwork? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("🎨 Thanks for using AI Artist Agent! Keep creating! ✨")
                break

if __name__ == "__main__":
    asyncio.run(main()) 