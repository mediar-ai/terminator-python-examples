#!/usr/bin/env python3
"""
Notepad automation test script
Tests text input and form automation
"""

import terminator

def test_notepad_basic():
    """Test basic notepad text input"""
    try:
        desktop = terminator.Desktop()
        print("Opening Notepad...")
        
        # Open notepad
        desktop.open_application('notepad')
        
        # Find text editor area
        editor = desktop.locator('window:Notepad').locator('name:Edit')
        editor.expect_visible()
        print("✓ Notepad is ready")
        
        # Type test text
        test_text = "Hello from Terminator SDK!\nThis is a test of desktop automation."
        print(f"Typing text: {test_text[:30]}...")
        editor.type_text(test_text)
        
        # Get text content to verify
        content = editor.get_text()
        print(f"✓ Text entered successfully")
        print(f"Content preview: {content.text[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Notepad basic test failed: {e}")
        return False

def test_notepad_form_automation():
    """Test form-like data entry in notepad"""
    try:
        desktop = terminator.Desktop()
        
        # Find editor (assuming notepad is still open)
        editor = desktop.locator('window:Notepad').locator('name:Edit')
        
        # Clear existing content
        editor.type_text("", clear=True)
        
        # Type structured form data
        form_data = """=== Contact Information ===
Name: John Doe
Email: john.doe@example.com
Phone: (555) 123-4567
Address: 123 Main St, Anytown, USA
Department: Engineering
Start Date: 2024-01-15

=== Notes ===
This is a test contact entry created by Terminator SDK.
The automation successfully filled out this form data.
"""
        
        print("Entering structured form data...")
        editor.type_text(form_data)
        
        # Verify content
        content = editor.get_text()
        if "John Doe" in content.text and "Engineering" in content.text:
            print("✓ Form data entered successfully")
            return True
        else:
            print("❌ Form data verification failed")
            return False
        
    except Exception as e:
        print(f"❌ Form automation test failed: {e}")
        return False

def test_element_attributes():
    """Test getting element attributes and state"""
    try:
        desktop = terminator.Desktop()
        
        # Find the editor element
        editor = desktop.locator('window:Notepad').locator('name:Edit')
        
        # Check if element is visible
        is_visible = editor.is_visible()
        print(f"✓ Editor visible: {is_visible}")
        
        # Get element bounds
        bounds = editor.get_bounds()
        print(f"✓ Editor bounds: x={bounds.x}, y={bounds.y}, size={bounds.width}x{bounds.height}")
        
        # Get all attributes
        attributes = editor.get_attributes()
        print(f"✓ Editor has {len(attributes)} attributes")
        
        return True
        
    except Exception as e:
        print(f"❌ Element attributes test failed: {e}")
        return False

if __name__ == "__main__":
    print("=== Notepad Automation Test ===\n")
    
    # Run basic notepad test
    success1 = test_notepad_basic()
    print()
    
    # Run form automation test
    success2 = test_notepad_form_automation()
    print()
    
    # Test element attributes
    success3 = test_element_attributes()
    
    if success1 and success2 and success3:
        print("\n🎉 All notepad tests passed!")
    else:
        print("\n❌ Some notepad tests failed") 