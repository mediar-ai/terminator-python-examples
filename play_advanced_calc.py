#!/usr/bin/env python3
"""
Advanced Calculator Automation - Mathematical wizardry!
Performs complex calculations and explores calculator features
"""

import asyncio
import terminator
import math

async def open_calculator():
    """Open Windows Calculator"""
    desktop = terminator.Desktop()
    print("🧮 Opening Calculator...")
    desktop.open_application('calc')
    await asyncio.sleep(2)
    return desktop

async def clear_calculator(desktop):
    """Clear the calculator"""
    try:
        clear_btn = desktop.locator('name:Clear')
        clear_btn.click()
        await asyncio.sleep(0.3)
        return True
    except Exception as e:
        print(f"⚠ Could not clear calculator: {e}")
        return False

async def perform_calculation(desktop, expression, expected=None):
    """Perform a calculation and optionally verify result"""
    print(f"🔢 Calculating: {expression}")
    
    try:
        # Parse and click the expression
        for char in expression:
            if char.isdigit():
                # Click number
                btn = desktop.locator(f'name:{char}')
                btn.click()
            elif char == '+':
                btn = desktop.locator('name:Plus')
                btn.click()
            elif char == '-':
                btn = desktop.locator('name:Minus')
                btn.click()
            elif char == '*':
                btn = desktop.locator('name:Multiply by')
                btn.click()
            elif char == '/':
                btn = desktop.locator('name:Divide by')
                btn.click()
            elif char == '=':
                btn = desktop.locator('name:Equals')
                btn.click()
            elif char == '.':
                btn = desktop.locator('name:Decimal separator')
                btn.click()
            elif char == '(':
                btn = desktop.locator('name:Open parenthesis')
                btn.click()
            elif char == ')':
                btn = desktop.locator('name:Close parenthesis')
                btn.click()
            
            await asyncio.sleep(0.2)
        
        # Click equals if not already in expression
        if '=' not in expression:
            equals_btn = desktop.locator('name:Equals')
            equals_btn.click()
            await asyncio.sleep(0.5)
        
        print(f"✓ Calculation completed: {expression}")
        
        if expected:
            print(f"  Expected: {expected}")
        
        return True
        
    except Exception as e:
        print(f"❌ Calculation failed: {e}")
        return False

async def try_scientific_functions(desktop):
    """Try to use scientific calculator functions"""
    try:
        print("🔬 Testing scientific functions...")
        
        # Try to switch to scientific mode
        menu_btn = desktop.locator('name:Menu')
        if menu_btn.is_visible():
            menu_btn.click()
            await asyncio.sleep(0.5)
            
            scientific_item = desktop.locator('name:Scientific')
            if scientific_item.is_visible():
                scientific_item.click()
                await asyncio.sleep(1)
                print("✓ Switched to Scientific mode")
        
        # Test square root of 16
        await clear_calculator(desktop)
        
        # Enter 16
        desktop.locator('name:1').click()
        await asyncio.sleep(0.2)
        desktop.locator('name:6').click()
        await asyncio.sleep(0.2)
        
        # Click square root
        try:
            sqrt_btn = desktop.locator('name:Square root')
            sqrt_btn.click()
            print("✓ Square root function used")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"⚠ Square root function not found: {e}")
        
        return True
        
    except Exception as e:
        print(f"⚠ Scientific functions failed: {e}")
        return False

async def memory_operations(desktop):
    """Test calculator memory functions"""
    try:
        print("💾 Testing memory operations...")
        
        # Clear and calculate 25
        await clear_calculator(desktop)
        desktop.locator('name:2').click()
        await asyncio.sleep(0.2)
        desktop.locator('name:5').click()
        await asyncio.sleep(0.2)
        
        # Store in memory (M+)
        try:
            m_plus = desktop.locator('name:Memory add')
            m_plus.click()
            print("✓ Stored 25 in memory")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"⚠ Memory add not found: {e}")
            return False
        
        # Clear and calculate 10
        await clear_calculator(desktop)
        desktop.locator('name:1').click()
        await asyncio.sleep(0.2)
        desktop.locator('name:0').click()
        await asyncio.sleep(0.2)
        
        # Add to memory result (=35)
        desktop.locator('name:Plus').click()
        await asyncio.sleep(0.2)
        
        try:
            m_recall = desktop.locator('name:Memory recall')
            m_recall.click()
            print("✓ Recalled from memory")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"⚠ Memory recall not found: {e}")
        
        desktop.locator('name:Equals').click()
        await asyncio.sleep(0.5)
        
        print("✓ Memory operations completed")
        return True
        
    except Exception as e:
        print(f"⚠ Memory operations failed: {e}")
        return False

async def stress_test_calculations(desktop):
    """Perform multiple rapid calculations"""
    print("⚡ Stress testing with rapid calculations...")
    
    calculations = [
        "123+456",
        "789-321", 
        "12*34",
        "144/12",
        "7*8*9",
        "100-25-25-25-25"
    ]
    
    for calc in calculations:
        await clear_calculator(desktop)
        await perform_calculation(desktop, calc)
        await asyncio.sleep(0.5)
    
    print("✓ Stress test completed!")

async def advanced_calculator_demo():
    """Main advanced calculator demonstration"""
    print("=== Advanced Calculator Automation Demo ===\n")
    
    try:
        desktop = await open_calculator()
        
        # Basic calculations
        await perform_calculation(desktop, "2+2", "4")
        await asyncio.sleep(1)
        
        await clear_calculator(desktop)
        await perform_calculation(desktop, "15*7", "105")
        await asyncio.sleep(1)
        
        await clear_calculator(desktop)
        await perform_calculation(desktop, "100/4", "25")
        await asyncio.sleep(1)
        
        # Try scientific functions
        await try_scientific_functions(desktop)
        await asyncio.sleep(1)
        
        # Test memory operations
        await memory_operations(desktop)
        await asyncio.sleep(1)
        
        # Stress test
        await stress_test_calculations(desktop)
        
        print("\n🧮 Advanced Calculator demo completed!")
        print("Calculator should show the results of various operations!")
        
    except Exception as e:
        print(f"❌ Advanced Calculator demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(advanced_calculator_demo()) 