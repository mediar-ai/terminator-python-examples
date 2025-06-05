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
    print("BASIC AUTOMATION:")
    print("1. 🎨 Paint Automation - Create digital art")
    print("2. 📁 File Explorer Fun - Navigate and organize")
    print("3. 🧮 Advanced Calculator - Mathematical wizardry")
    print("4. 🔄 Ultimate Workflow - Multi-app coordination")
    print("5. 📝 Simple Example - Basic demo")
    print("6. 🧪 Final Test Suite - Comprehensive testing")
    print()
    print("AI-POWERED AUTOMATION:")
    print("7. 🤖 Simple AI Demo - AI + Notepad/Calculator")
    print("8. 🧠 Advanced AI Agent - Smart workflow planning")
    print()
    print("ALL DEMOS:")
    print("9. 🎯 All Basic Scripts - Run everything!")
    print("A. 🌟 All AI Demos - AI-powered automation")
    print("B. 🚀 EVERYTHING - All demos (basic + AI)")
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

async def run_all_basic_scripts():
    """Run all the basic automation scripts in sequence"""
    scripts = [
        "example.py",
        "play_advanced_calc.py",
        "play_paint.py",
        "play_file_explorer.py",
        "play_workflow.py"
    ]
    
    print("🎪 RUNNING ALL BASIC SCRIPTS!")
    print("="*50)
    print("This will run all basic automation demos in sequence.")
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
    
    print(f"\n🎊 ALL BASIC DEMOS COMPLETED!")
    print(f"Success rate: {success_count}/{len(scripts)} scripts")

async def run_all_ai_scripts():
    """Run all AI-powered automation scripts"""
    scripts = [
        "ai_simple.py",
        "ai_automation.py"
    ]
    
    print("🧠 RUNNING ALL AI DEMOS!")
    print("="*50)
    print("This will run all AI-powered automation demos.")
    print("Make sure Ollama is running and models are downloaded! 🤖\n")
    
    # Check if Ollama is likely available
    print("🔍 Checking AI setup...")
    try:
        import ollama
        print("✓ Ollama Python package found")
    except ImportError:
        print("❌ Ollama package not found - install with: pip install ollama")
        return
    
    success_count = 0
    
    for i, script in enumerate(scripts, 1):
        print(f"\n🎬 AI Demo {i}/{len(scripts)}: {script}")
        success = await run_script(script)
        if success:
            success_count += 1
        
        # Pause between scripts
        if i < len(scripts):
            print("\n⏸️ Pausing for 5 seconds before next AI demo...")
            await asyncio.sleep(5)
    
    print(f"\n🤖 ALL AI DEMOS COMPLETED!")
    print(f"Success rate: {success_count}/{len(scripts)} scripts")

async def run_everything():
    """Run absolutely everything - the ultimate demo!"""
    print("🚀 ULTIMATE AUTOMATION SHOWCASE!")
    print("="*60)
    print("Running EVERY demo: Basic + AI-powered automation")
    print("This is the complete showcase of automation capabilities!")
    print("="*60)
    
    print("\n🎬 PHASE 1: Basic Automation Demos")
    print("-" * 40)
    await run_all_basic_scripts()
    
    print("\n" + "="*60)
    print("🧠 PHASE 2: AI-Powered Automation Demos")
    print("-" * 40)
    await run_all_ai_scripts()
    
    print("\n" + "="*60)
    print("🎊 ULTIMATE SHOWCASE COMPLETED!")
    print("="*60)
    print("You've just witnessed the full power of:")
    print("• Desktop automation with Terminator SDK")
    print("• AI-generated content and workflows")
    print("• Multi-application coordination")
    print("• Creative and practical automation examples")
    print("\nWelcome to the future of intelligent automation! 🌟")

async def main():
    """Main menu loop"""
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-9, A, B): ").strip().upper()
            
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
                await run_script("ai_simple.py")
                
            elif choice == "8":
                await run_script("ai_automation.py")
                
            elif choice == "9":
                await run_all_basic_scripts()
                
            elif choice == "A":
                await run_all_ai_scripts()
                
            elif choice == "B":
                await run_everything()
                
            else:
                print("\n❌ Invalid choice! Please enter 0-9, A, or B.")
                
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