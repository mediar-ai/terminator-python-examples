#!/usr/bin/env python3
"""
Calculator automation test script
Tests mathematical operations using Windows Calculator
"""

import terminator

def automate_calculator():
    """Automate calculator to perform 7 + 7 = 14"""
    try:
        # Create desktop instance
        desktop = terminator.Desktop()
        print("Opening Calculator...")
        
        # Open calculator
        desktop.open_application('calc')
        
        # Wait for calculator to be ready
        calc_window = desktop.locator('window:Calculator')
        calc_window.expect_visible()
        print("✓ Calculator is ready")
        
        # Perform calculation: 7 + 7 = 14
        print("Performing calculation: 7 + 7")
        desktop.locator('name:Seven').click()
        desktop.locator('name:Plus').click()
        desktop.locator('name:Seven').click()
        desktop.locator('name:Equals').click()
        
        # Get result
        result = desktop.locator('automationid:CalculatorResults').get_text()
        print(f"✓ Calculation result: {result.text}")
        
        # Verify result
        if "14" in result.text:
            print("🎉 Calculator test passed!")
            return True
        else:
            print(f"❌ Unexpected result: {result.text}")
            return False
        
    except Exception as e:
        print(f"❌ Calculator automation failed: {e}")
        return False

def test_calculator_multiple_operations():
    """Test multiple calculator operations"""
    try:
        desktop = terminator.Desktop()
        
        # Clear calculator first
        desktop.locator('name:Clear').click()
        print("Calculator cleared")
        
        # Test: 5 * 3 = 15
        print("Testing: 5 * 3")
        desktop.locator('name:Five').click()
        desktop.locator('name:Multiply by').click()
        desktop.locator('name:Three').click()
        desktop.locator('name:Equals').click()
        
        result = desktop.locator('automationid:CalculatorResults').get_text()
        print(f"✓ Result: {result.text}")
        
        return "15" in result.text
        
    except Exception as e:
        print(f"❌ Multiple operations test failed: {e}")
        return False

if __name__ == "__main__":
    print("=== Calculator Automation Test ===\n")
    
    # Run basic calculation test
    success1 = automate_calculator()
    print()
    
    # Run multiple operations test
    success2 = test_calculator_multiple_operations()
    
    if success1 and success2:
        print("\n🎉 All calculator tests passed!")
    else:
        print("\n❌ Some calculator tests failed") 