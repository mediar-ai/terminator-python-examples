#!/usr/bin/env python3
"""
Test Capture Functionality - Test if element.capture() works
"""

import asyncio
import terminator
import time
from datetime import datetime

async def test_capture_functionality():
    """Test if we can capture screenshots from Paint"""
    print("📸 TESTING TERMINATOR CAPTURE FUNCTIONALITY")
    print("="*50)
    
    try:
        # Open Paint
        print("1. Opening MS Paint...")
        desktop = terminator.Desktop()
        desktop.open_application('mspaint')
        await asyncio.sleep(3)
        
        # Draw something simple first
        print("2. Drawing a simple shape...")
        canvas = desktop.locator('name:Canvas')
        
        # Draw a simple line
        canvas.mouse_click_and_hold(300, 200)
        await asyncio.sleep(0.1)
        canvas.mouse_move(500, 300)
        canvas.mouse_release()
        await asyncio.sleep(1)
        
        # Try to capture the canvas
        print("3. Attempting to capture canvas...")
        try:
            screenshot_data = canvas.capture()
            print(f"   ✅ Capture successful! Data size: {len(screenshot_data)} bytes")
            
            # Save the screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"test_capture_{timestamp}.png"
            
            with open(filename, 'wb') as f:
                f.write(screenshot_data)
            
            print(f"   💾 Screenshot saved as: {filename}")
            
        except Exception as capture_error:
            print(f"   ❌ Capture failed: {str(capture_error)}")
            
            # Try alternative capture methods
            print("4. Trying alternative capture methods...")
            
            try:
                # Try capturing the whole Paint window
                paint_window = desktop.locator('class:MSPaintApp')
                window_data = paint_window.capture()
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"test_window_capture_{timestamp}.png"
                
                with open(filename, 'wb') as f:
                    f.write(window_data)
                
                print(f"   ✅ Window capture successful! Saved as: {filename}")
                
            except Exception as window_error:
                print(f"   ❌ Window capture also failed: {str(window_error)}")
                
                # Try desktop screenshot
                try:
                    desktop_data = desktop.capture()
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"test_desktop_capture_{timestamp}.png"
                    
                    with open(filename, 'wb') as f:
                        f.write(desktop_data)
                    
                    print(f"   ✅ Desktop capture successful! Saved as: {filename}")
                    
                except Exception as desktop_error:
                    print(f"   ❌ Desktop capture also failed: {str(desktop_error)}")
        
        print("\n📋 CAPTURE TEST SUMMARY:")
        print("- Tested canvas.capture()")
        print("- Tested paint_window.capture()")  
        print("- Tested desktop.capture()")
        print("- Check the generated .png files!")
        
    except Exception as e:
        print(f"💥 Overall test failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_capture_functionality()) 