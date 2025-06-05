#!/usr/bin/env python3
"""
Check Terminator API - Inspect what methods are actually available
"""

import terminator

def check_terminator_api():
    """Check what methods are available in terminator Desktop"""
    print("🔍 CHECKING TERMINATOR API")
    print("="*50)
    
    desktop = terminator.Desktop()
    
    print("📋 Available methods in terminator.Desktop:")
    methods = [method for method in dir(desktop) if not method.startswith('_')]
    
    for i, method in enumerate(methods, 1):
        print(f"  {i:2d}. {method}")
    
    print(f"\n📊 Total methods: {len(methods)}")
    
    # Test specific methods we need
    print("\n🎯 Testing specific methods:")
    
    test_methods = ['move_mouse', 'mouse_down', 'mouse_up', 'click', 'type_text']
    
    for method_name in test_methods:
        if hasattr(desktop, method_name):
            print(f"  ✅ {method_name} - Available")
        else:
            print(f"  ❌ {method_name} - NOT AVAILABLE")
    
    # Check for alternatives
    print("\n🔍 Checking for mouse-related methods:")
    mouse_methods = [m for m in methods if 'mouse' in m.lower() or 'click' in m.lower() or 'move' in m.lower()]
    if mouse_methods:
        for method in mouse_methods:
            print(f"  🖱️  {method}")
    else:
        print("  ❌ No mouse methods found!")

if __name__ == "__main__":
    check_terminator_api() 