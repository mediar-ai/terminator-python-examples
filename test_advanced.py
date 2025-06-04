#!/usr/bin/env python3
"""
Advanced test script for Terminator SDK
Tests expectations, error handling, and complex scenarios
"""

import terminator
import time

def test_expectations():
    """Test expectation methods for waiting conditions"""
    try:
        desktop = terminator.Desktop()
        print("Testing expectations and timeouts...")
        
        # Open calculator if not already open
        desktop.open_application('calc')
        
        # Test expect_visible with timeout
        calc_window = desktop.locator('window:Calculator')
        element = calc_window.expect_visible(timeout=5000)
        print("✓ expect_visible() worked")
        
        # Test expect_enabled
        seven_btn = desktop.locator('name:Seven')
        seven_btn.expect_enabled(timeout=3000)
        print("✓ expect_enabled() worked")
        
        # Click a button and test text expectations
        seven_btn.click()
        result_display = desktop.locator('automationid:CalculatorResults')
        result_display.expect_text_contains('7', timeout=3000)
        print("✓ expect_text_contains() worked")
        
        return True
        
    except Exception as e:
        print(f"❌ Expectations test failed: {e}")
        return False

def test_chained_selectors():
    """Test chained selector patterns"""
    try:
        desktop = terminator.Desktop()
        print("Testing chained selectors...")
        
        # Complex chained selector
        button = desktop.locator('window:Calculator').locator('role:Button').locator('name:Seven')
        if button.is_visible():
            print("✓ Chained selector found element")
        
        # Alternative selector patterns
        patterns = [
            'name:Seven',
            'role:Button',
            'automationid:CalculatorResults'
        ]
        
        for pattern in patterns:
            try:
                element = desktop.locator(pattern)
                is_visible = element.is_visible()
                print(f"✓ Pattern '{pattern}': visible={is_visible}")
            except Exception as e:
                print(f"⚠ Pattern '{pattern}' failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Chained selectors test failed: {e}")
        return False

def test_error_handling():
    """Test proper error handling"""
    try:
        desktop = terminator.Desktop()
        print("Testing error handling...")
        
        # Test with non-existent element
        try:
            desktop.locator('name:DoesNotExist').click()
            print("❌ Expected error but none occurred")
            return False
        except Exception as e:
            print(f"✓ Properly caught error: {type(e).__name__}")
        
        # Test with invalid selector
        try:
            desktop.locator('invalid:selector:pattern').is_visible()
            print("❌ Expected error but none occurred")
            return False
        except Exception as e:
            print(f"✓ Properly caught invalid selector error: {type(e).__name__}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error handling test failed: {e}")
        return False

def test_url_opening():
    """Test opening URLs"""
    try:
        desktop = terminator.Desktop()
        print("Testing URL opening...")
        
        # Open GitHub URL from documentation
        desktop.open_url('https://github.com/mediar-ai/terminator')
        print("✓ URL opened successfully")
        
        # Wait a moment for browser to load
        time.sleep(2)
        
        return True
        
    except Exception as e:
        print(f"❌ URL opening test failed: {e}")
        return False

def test_comprehensive_workflow():
    """Test a comprehensive automation workflow"""
    try:
        desktop = terminator.Desktop()
        print("Running comprehensive workflow test...")
        
        # 1. Open calculator
        desktop.open_application('calc')
        calc_window = desktop.locator('window:Calculator')
        calc_window.expect_visible()
        
        # 2. Perform calculation
        desktop.locator('name:Nine').click()
        desktop.locator('name:Multiply by').click()
        desktop.locator('name:Six').click()
        desktop.locator('name:Equals').click()
        
        # 3. Verify result
        result = desktop.locator('automationid:CalculatorResults').get_text()
        expected = "54"
        
        if expected in result.text:
            print(f"✓ Calculation verified: {result.text}")
        else:
            print(f"❌ Unexpected calculation result: {result.text}")
            return False
        
        # 4. Open notepad and record result
        desktop.open_application('notepad')
        editor = desktop.locator('window:Notepad').locator('name:Edit')
        editor.expect_visible()
        
        # 5. Document the calculation
        documentation = f"""Terminator SDK Test Results
========================

Calculator Test: PASSED
Calculation: 9 × 6 = {result.text.strip()}
Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}

This demonstrates:
- Application launching
- Element location and interaction
- Text input automation
- Result verification
"""
        
        editor.type_text(documentation)
        print("✓ Results documented in Notepad")
        
        return True
        
    except Exception as e:
        print(f"❌ Comprehensive workflow test failed: {e}")
        return False

if __name__ == "__main__":
    print("=== Advanced Terminator SDK Tests ===\n")
    
    tests = [
        ("Expectations", test_expectations),
        ("Chained Selectors", test_chained_selectors),
        ("Error Handling", test_error_handling),
        ("URL Opening", test_url_opening),
        ("Comprehensive Workflow", test_comprehensive_workflow)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"--- {test_name} ---")
        success = test_func()
        results.append((test_name, success))
        print()
    
    # Summary
    print("=== Test Summary ===")
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✓ PASS" if success else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All advanced tests passed!")
    else:
        print("⚠ Some tests failed - check logs above") 