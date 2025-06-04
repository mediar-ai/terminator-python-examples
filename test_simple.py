#!/usr/bin/env python3
"""
Simple test script for Terminator SDK
Tests basic functionality without async operations
"""

import terminator
import time

def test_simple_functionality():
    """Test simple SDK functionality"""
    try:
        # Create desktop instance
        desktop = terminator.Desktop()
        print("✓ Terminator Desktop instance created successfully")
        
        # Test opening a simple application
        print("Opening Calculator...")
        desktop.open_application('calc')
        print("✓ Calculator opened successfully")
        
        # Wait a moment for app to load
        time.sleep(2)
        
        # Test locating elements without expectations
        calc_window = desktop.locator('window:Calculator')
        print("✓ Calculator window locator created")
        
        # Test visibility check
        is_visible = calc_window.is_visible()
        print(f"✓ Calculator window visible: {is_visible}")
        
        # Test clicking a button
        seven_btn = desktop.locator('name:Seven')
        seven_btn.click()
        print("✓ Clicked Seven button")
        
        # Test another button
        plus_btn = desktop.locator('name:Plus')
        plus_btn.click()
        print("✓ Clicked Plus button")
        
        # Click seven again
        seven_btn.click()
        print("✓ Clicked Seven button again")
        
        # Click equals
        equals_btn = desktop.locator('name:Equals')
        equals_btn.click()
        print("✓ Clicked Equals button")
        
        # Get result
        time.sleep(1)  # Wait for calculation
        result = desktop.locator('automationid:CalculatorResults').get_text()
        print(f"✓ Calculation result: {result.text}")
        
        if "14" in result.text:
            print("🎉 Calculator test passed! (7 + 7 = 14)")
        else:
            print(f"⚠ Unexpected result: {result.text}")
        
        print("\n🎉 Simple functionality test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=== Terminator SDK Simple Test ===\n")
    test_simple_functionality() 