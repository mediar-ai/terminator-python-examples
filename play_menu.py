#!/usr/bin/env python3
"""
Terminator SDK Playground Menu
Interactive menu to choose fun automation demos
"""

import asyncio
import subprocess
import sys

def display_menu():
    """Display the interactive menu"""
    print("🤖 TERMINATOR SDK PLAYGROUND")
    print("="*50)
    print("Choose your automation adventure:")
    print()
    print("1. 🎨 Paint Automation - Create digital art")
    print("2. 📁 File Explorer Fun - Navigate and organize")
    print("3. 🧮 Advanced Calculator - Mathematical wizardry")
    print("4. 🔄 Ultimate Workflow - Multi-app coordination")
    print("5. 📝 Simple Example - Basic demo")
    print("6. 🧪 Final Test Suite - Comprehensive testing")
    print("7. 🎯 All Fun Scripts - Run everything!")
    print()
    print("0. Exit")
    print("="*50)

async def run_script(script_name):
    """Run a Python script and display output"""
    try:
        print(f"\n🚀 Launching: {script_name}")
        print("-" * 40)
        
        # Run the script
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=False, 
                              text=True,
                              cwd='.')
        
        print(f"\n✅ {script_name} completed (exit code: {result.returncode})")
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Failed to run {script_name}: {e}")
        return False

async def run_all_fun_scripts():
    """Run all the fun automation scripts in sequence"""
    scripts = [
        "example.py",
        "play_advanced_calc.py",
        "play_paint.py",
        "play_file_explorer.py",
        "play_workflow.py"
    ]
    
    print("🎪 RUNNING ALL FUN SCRIPTS!")
    print("="*50)
    print("This will run all automation demos in sequence.")
    print("Grab some popcorn and watch the magic happen! 🍿\n")
    
    success_count = 0
    
    for i, script in enumerate(scripts, 1):
        print(f"\n🎬 Demo {i}/{len(scripts)}: {script}")
        success = await run_script(script)
        if success:
            success_count += 1
        
        # Pause between scripts
        if i < len(scripts):
            print("\n⏸️ Pausing for 3 seconds before next demo...")
            await asyncio.sleep(3)
    
    print(f"\n🎊 ALL DEMOS COMPLETED!")
    print(f"Success rate: {success_count}/{len(scripts)} scripts")
    print("Check your screen for all the applications and automation results! 🎉")

async def main():
    """Main menu loop"""
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == "0":
                print("\n👋 Thanks for playing with Terminator SDK!")
                print("Happy automating! 🤖✨")
                break
                
            elif choice == "1":
                await run_script("play_paint.py")
                
            elif choice == "2":
                await run_script("play_file_explorer.py")
                
            elif choice == "3":
                await run_script("play_advanced_calc.py")
                
            elif choice == "4":
                await run_script("play_workflow.py")
                
            elif choice == "5":
                await run_script("example.py")
                
            elif choice == "6":
                await run_script("test_final.py")
                
            elif choice == "7":
                await run_all_fun_scripts()
                
            else:
                print("\n❌ Invalid choice! Please enter 0-7.")
                
        except KeyboardInterrupt:
            print("\n\n⏹️ Menu interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
        
        # Pause before showing menu again
        if choice != "0":
            input("\n📱 Press Enter to return to menu...")
            print("\n" + "="*50)

if __name__ == "__main__":
    print("🎮 Initializing Terminator SDK Playground...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Playground closed. See you next time!")
    except Exception as e:
        print(f"\n❌ Playground error: {e}")
        print("Try running individual scripts directly if issues persist.") 