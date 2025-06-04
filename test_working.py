#!/usr/bin/env python3
"""
Working test script for Terminator SDK
Based on the exact examples from the GitHub repository
"""

import terminator

def test_basic_working():
    """Test the exact example from the GitHub repository"""
    try:
        print("Creating Desktop instance...")
        desktop = terminator.Desktop()
        print("✓ Desktop instance created")
        
        print("Opening Calculator...")
        desktop.open_application('calc')
        print("✓ Calculator opened")
        
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

def test_calculator_math():
    """Test a simple calculation"""
    try:
        desktop = terminator.Desktop()
        
        print("Performing calculation: 7 + 7")
        
        # Click Seven
        seven = desktop.locator('name:Seven')
        seven.click()
        print("✓ First 7 clicked")
        
        # Click Plus
        plus = desktop.locator('name:Plus')
        plus.click()
        print("✓ Plus clicked")
        
        # Click Seven again
        seven.click()
        print("✓ Second 7 clicked")
        
        # Click Equals
        equals = desktop.locator('name:Equals')
        equals.click()
        print("✓ Equals clicked")
        
        print("🎉 Calculation completed!")
        return True
        
    except Exception as e:
        print(f"❌ Calculation test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=== Terminator SDK Working Test ===\n")
    
    success1 = test_basic_working()
    print()
    
    if success1:
        success2 = test_calculator_math()
        
        if success1 and success2:
            print("\n🎉 All tests passed! SDK is working correctly.")
        else:
            print("\n⚠ Some tests had issues.")
    else:
        print("\n❌ Basic test failed, skipping calculator test.") 