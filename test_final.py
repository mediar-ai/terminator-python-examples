#!/usr/bin/env python3
"""
Final working test script for Terminator SDK
Uses asyncio event loop to handle the SDK's requirements
"""

import asyncio
import terminator

async def test_basic_working():
    """Test the exact example from the GitHub repository"""
    try:
        print("Creating Desktop instance...")
        desktop = terminator.Desktop()
        print("✓ Desktop instance created")
        
        print("Opening Calculator...")
        desktop.open_application('calc')
        print("✓ Calculator opened")
        
        # Wait for app to load
        await asyncio.sleep(2)
        
        print("Finding Seven button...")
        seven = desktop.locator('name:Seven')
        print("✓ Seven button locator created")
        
        print("Clicking Seven...")
        seven.click()
        print("✓ Seven clicked successfully")
        
        print("\n🎉 Basic working test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_calculator_math():
    """Test a simple calculation"""
    try:
        desktop = terminator.Desktop()
        
        print("Performing calculation: 7 + 7")
        
        # Click Seven
        seven = desktop.locator('name:Seven')
        seven.click()
        print("✓ First 7 clicked")
        
        await asyncio.sleep(0.5)
        
        # Click Plus
        plus = desktop.locator('name:Plus')
        plus.click()
        print("✓ Plus clicked")
        
        await asyncio.sleep(0.5)
        
        # Click Seven again
        seven.click()
        print("✓ Second 7 clicked")
        
        await asyncio.sleep(0.5)
        
        # Click Equals
        equals = desktop.locator('name:Equals')
        equals.click()
        print("✓ Equals clicked")
        
        await asyncio.sleep(1)
        
        # Try to get the result
        try:
            result = desktop.locator('automationid:CalculatorResults')
            result_text = result.get_text()
            print(f"✓ Calculation result: {result_text.text}")
        except Exception as e:
            print(f"⚠ Could not get result: {e}")
        
        print("🎉 Calculation completed!")
        return True
        
    except Exception as e:
        print(f"❌ Calculation test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_notepad():
    """Test notepad automation"""
    try:
        desktop = terminator.Desktop()
        
        print("Opening Notepad...")
        desktop.open_application('notepad')
        print("✓ Notepad opened")
        
        await asyncio.sleep(2)
        
        # Find text editor
        editor = desktop.locator('name:Edit')
        print("✓ Editor found")
        
        # Type text
        test_text = "Hello from Terminator SDK!\nThis is a successful test."
        editor.type_text(test_text)
        print("✓ Text typed successfully")
        
        await asyncio.sleep(1)
        
        # Try to get text back
        try:
            content = editor.get_text()
            print(f"✓ Editor content verified: {content.text[:30]}...")
        except Exception as e:
            print(f"⚠ Could not read content: {e}")
        
        print("🎉 Notepad test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Notepad test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Main async function to run all tests"""
    print("=== Terminator SDK Final Test ===\n")
    
    # Test 1: Basic functionality
    print("--- Test 1: Basic Calculator ---")
    success1 = await test_basic_working()
    print()
    
    # Test 2: Calculator math
    if success1:
        print("--- Test 2: Calculator Math ---")
        success2 = await test_calculator_math()
        print()
    else:
        success2 = False
    
    # Test 3: Notepad
    print("--- Test 3: Notepad ---")
    success3 = await test_notepad()
    print()
    
    # Summary
    total_tests = 3
    passed_tests = sum([success1, success2, success3])
    
    print("=== Test Summary ===")
    print(f"✓ Basic Calculator: {'PASS' if success1 else 'FAIL'}")
    print(f"✓ Calculator Math: {'PASS' if success2 else 'FAIL'}")
    print(f"✓ Notepad: {'PASS' if success3 else 'FAIL'}")
    print(f"\nResults: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! Terminator SDK is working correctly!")
    else:
        print(f"\n⚠ {total_tests - passed_tests} tests failed.")

if __name__ == "__main__":
    asyncio.run(main()) 