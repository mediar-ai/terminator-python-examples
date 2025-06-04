#!/usr/bin/env python3
"""
Basic test script for Terminator SDK
Tests basic functionality and SDK installation
"""

import terminator

def test_basic_functionality():
    """Test basic SDK functionality"""
    try:
        # Create desktop instance
        desktop = terminator.Desktop()
        print("✓ Terminator Desktop instance created successfully")
        
        # Test opening a simple application
        print("Opening Calculator...")
        desktop.open_application('calc')
        print("✓ Calculator opened successfully")
        
        # Test locating the calculator window
        calc_window = desktop.locator('window:Calculator')
        calc_window.expect_visible()
        print("✓ Calculator window located and visible")
        
        print("\n🎉 Basic functionality test passed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("=== Terminator SDK Basic Test ===\n")
    test_basic_functionality() 