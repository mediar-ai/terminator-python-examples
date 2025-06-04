#!/usr/bin/env python3
"""
Simple example script for Terminator SDK
Demonstrates the basic usage pattern that works
"""

import asyncio
import terminator

async def calculator_demo():
    """Simple calculator demonstration"""
    print("🔢 Calculator Demo")
    print("Opening calculator and performing 5 + 3...")
    
    # Create desktop instance
    desktop = terminator.Desktop()
    
    # Open calculator
    desktop.open_application('calc')
    
    # Wait for app to load
    await asyncio.sleep(2)
    
    # Perform calculation: 5 + 3
    desktop.locator('name:Five').click()
    await asyncio.sleep(0.3)
    
    desktop.locator('name:Plus').click()
    await asyncio.sleep(0.3)
    
    desktop.locator('name:Three').click()
    await asyncio.sleep(0.3)
    
    desktop.locator('name:Equals').click()
    await asyncio.sleep(0.5)
    
    print("✅ Calculation completed: 5 + 3 = 8")

async def notepad_demo():
    """Simple notepad demonstration"""
    print("\n📝 Notepad Demo")
    print("Opening notepad and typing text...")
    
    # Create desktop instance
    desktop = terminator.Desktop()
    
    # Open notepad
    desktop.open_application('notepad')
    
    # Wait for app to load
    await asyncio.sleep(2)
    
    # Find text editor and type
    editor = desktop.locator('name:Edit')
    editor.type_text("Hello World from Terminator SDK!\n\nThis is automated text input.")
    
    print("✅ Text typed successfully!")

async def main():
    """Main demo function"""
    print("🤖 Terminator SDK Demo\n")
    
    try:
        # Run calculator demo
        await calculator_demo()
        
        # Run notepad demo  
        await notepad_demo()
        
        print("\n🎉 Demo completed successfully!")
        print("\nYou should now see:")
        print("1. Calculator showing the result of 5 + 3")
        print("2. Notepad with automated text input")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # This is the key part - using asyncio.run() to provide the event loop
    asyncio.run(main()) 