#!/usr/bin/env python3
"""
Check Locator API - See what methods are available on locator objects
"""

import terminator
import time

def check_locator_api():
    """Check what methods are available on locator objects"""
    print("🔍 CHECKING TERMINATOR LOCATOR API")
    print("="*50)
    
    desktop = terminator.Desktop()
    
    # Open Paint first
    print("Opening Paint...")
    desktop.open_application('mspaint')
    time.sleep(3)
    
    # Create a locator
    print("\n📍 Creating locator...")
    try:
        # Try to get a canvas or any element
        locator = desktop.locator('name:Canvas')
        print(f"Locator type: {type(locator)}")
        
        print("\n📋 Available methods on locator:")
        methods = [method for method in dir(locator) if not method.startswith('_')]
        
        for i, method in enumerate(methods, 1):
            print(f"  {i:2d}. {method}")
        
        print(f"\n📊 Total methods: {len(methods)}")
        
        # Test specific methods we need for drawing
        print("\n🎯 Testing drawing-related methods:")
        
        test_methods = ['click', 'double_click', 'right_click', 'drag', 'move_to', 'type_text', 'send_keys']
        
        for method_name in test_methods:
            if hasattr(locator, method_name):
                print(f"  ✅ {method_name} - Available")
            else:
                print(f"  ❌ {method_name} - NOT AVAILABLE")
        
        # Check for mouse-related methods
        print("\n🔍 Mouse/interaction methods:")
        interaction_methods = [m for m in methods if any(word in m.lower() for word in ['click', 'drag', 'move', 'mouse', 'type', 'send'])]
        if interaction_methods:
            for method in interaction_methods:
                print(f"  🖱️  {method}")
        else:
            print("  ❌ No interaction methods found!")
            
    except Exception as e:
        print(f"❌ Error creating locator: {e}")
        
        # Try a different approach
        print("\n🔄 Trying different locator...")
        try:
            # Try to find any element
            locator = desktop.locator('role:Button')
            print(f"Button locator type: {type(locator)}")
            
            methods = [method for method in dir(locator) if not method.startswith('_')]
            print(f"Button locator methods: {methods[:10]}...")  # Show first 10
            
        except Exception as e2:
            print(f"❌ Also failed: {e2}")

if __name__ == "__main__":
    check_locator_api() 