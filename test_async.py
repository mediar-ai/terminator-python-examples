#!/usr/bin/env python3
"""
Async test script for Terminator SDK
Tests functionality using async/await properly
"""

import asyncio
import terminator

async def test_async_functionality():
    """Test async SDK functionality"""
    try:
        # Create desktop instance
        desktop = terminator.Desktop()
        print("✓ Terminator Desktop instance created successfully")
        
        # Test opening a simple application
        print("Opening Calculator...")
        await desktop.open_application('calc')
        print("✓ Calculator opened successfully")
        
        # Wait a moment for app to load
        await asyncio.sleep(2)
        
        # Test locating elements
        calc_window = desktop.locator('window:Calculator')
        print("✓ Calculator window locator created")
        
        # Test visibility check
        is_visible = await calc_window.is_visible()
        print(f"✓ Calculator window visible: {is_visible}")
        
        # Test clicking a button
        seven_btn = desktop.locator('name:Seven')
        await seven_btn.click()
        print("✓ Clicked Seven button")
        
        # Test another button
        plus_btn = desktop.locator('name:Plus')
        await plus_btn.click()
        print("✓ Clicked Plus button")
        
        # Click seven again
        await seven_btn.click()
        print("✓ Clicked Seven button again")
        
        # Click equals
        equals_btn = desktop.locator('name:Equals')
        await equals_btn.click()
        print("✓ Clicked Equals button")
        
        # Get result
        await asyncio.sleep(1)  # Wait for calculation
        result_locator = desktop.locator('automationid:CalculatorResults')
        result = await result_locator.get_text()
        print(f"✓ Calculation result: {result.text}")
        
        if "14" in result.text:
            print("🎉 Calculator test passed! (7 + 7 = 14)")
        else:
            print(f"⚠ Unexpected result: {result.text}")
        
        print("\n🎉 Async functionality test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Main async function"""
    print("=== Terminator SDK Async Test ===\n")
    await test_async_functionality()

if __name__ == "__main__":
    asyncio.run(main()) 