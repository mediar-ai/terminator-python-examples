#!/usr/bin/env python3
"""
File Explorer automation - Navigate and organize files!
Automates Windows File Explorer for various tasks
"""

import asyncio
import terminator

async def open_explorer():
    """Open Windows File Explorer"""
    desktop = terminator.Desktop()
    print("📁 Opening File Explorer...")
    desktop.open_application('explorer')
    await asyncio.sleep(2)
    return desktop

async def navigate_to_desktop(desktop):
    """Navigate to Desktop folder"""
    try:
        # Click on Desktop in the sidebar
        desktop_item = desktop.locator('name:Desktop')
        desktop_item.click()
        print("✓ Navigated to Desktop")
        await asyncio.sleep(1)
        return True
    except Exception as e:
        print(f"⚠ Could not navigate to Desktop: {e}")
        return False

async def create_new_folder(desktop, folder_name):
    """Create a new folder"""
    try:
        # Right-click in empty space
        explorer_window = desktop.locator('window:File Explorer')
        
        # Try to find the main content area
        content_area = desktop.locator('name:Items View')
        if not content_area.is_visible():
            content_area = explorer_window
        
        # Right-click to open context menu
        print(f"📂 Creating folder: {folder_name}")
        # Note: This is simplified - actual right-click might need coordinates
        
        # Try to use Ctrl+Shift+N shortcut instead
        desktop.key_combination(['ctrl', 'shift', 'n'])
        await asyncio.sleep(1)
        
        # Type the folder name
        desktop.type_text(folder_name)
        desktop.key('enter')
        
        print(f"✓ Folder '{folder_name}' created")
        await asyncio.sleep(1)
        return True
        
    except Exception as e:
        print(f"⚠ Could not create folder: {e}")
        return False

async def create_text_file(desktop, filename):
    """Create a new text file"""
    try:
        print(f"📄 Creating text file: {filename}")
        
        # Use context menu approach
        explorer_window = desktop.locator('window:File Explorer')
        
        # Try keyboard shortcut for new file
        # This might vary by Windows version
        
        # Alternative: Open notepad and save to current location
        notepad_desktop = terminator.Desktop()
        notepad_desktop.open_application('notepad')
        await asyncio.sleep(2)
        
        # Type some content
        editor = notepad_desktop.locator('name:Edit')
        content = f"""This file was created by Terminator SDK automation!

Filename: {filename}
Created: Automatically
Purpose: Testing file creation capabilities

Pretty cool, right? 🤖
"""
        editor.type_text(content)
        
        # Save file (Ctrl+S)
        notepad_desktop.key_combination(['ctrl', 's'])
        await asyncio.sleep(1)
        
        # Type filename in save dialog
        notepad_desktop.type_text(filename)
        notepad_desktop.key('enter')
        
        print(f"✓ Text file '{filename}' created")
        await asyncio.sleep(1)
        
        # Close notepad
        notepad_desktop.key_combination(['alt', 'f4'])
        
        return True
        
    except Exception as e:
        print(f"⚠ Could not create text file: {e}")
        return False

async def explore_folders(desktop):
    """Explore different folders"""
    try:
        folders_to_visit = ['Documents', 'Pictures', 'Downloads']
        
        for folder in folders_to_visit:
            try:
                print(f"🗂️ Visiting {folder}...")
                folder_item = desktop.locator(f'name:{folder}')
                folder_item.click()
                await asyncio.sleep(1)
                print(f"✓ Visited {folder}")
            except Exception as e:
                print(f"⚠ Could not visit {folder}: {e}")
        
        return True
        
    except Exception as e:
        print(f"⚠ Folder exploration failed: {e}")
        return False

async def search_files(desktop, search_term):
    """Search for files"""
    try:
        print(f"🔍 Searching for: {search_term}")
        
        # Click in search box
        search_box = desktop.locator('name:Search')
        if not search_box.is_visible():
            # Try alternative search box names
            search_box = desktop.locator('name:Search Box')
        
        search_box.click()
        await asyncio.sleep(0.5)
        
        # Type search term
        desktop.type_text(search_term)
        desktop.key('enter')
        
        print(f"✓ Search initiated for '{search_term}'")
        await asyncio.sleep(2)
        
        return True
        
    except Exception as e:
        print(f"⚠ Search failed: {e}")
        return False

async def file_explorer_demo():
    """Main file explorer demonstration"""
    print("=== File Explorer Automation Demo ===\n")
    
    try:
        desktop = await open_explorer()
        
        # Navigate to Desktop
        await navigate_to_desktop(desktop)
        
        # Create a test folder
        await create_new_folder(desktop, "TerminatorSDK_Test")
        
        # Create a text file
        await create_text_file(desktop, "terminator_test.txt")
        
        # Explore some folders
        await explore_folders(desktop)
        
        # Search for something
        await search_files(desktop, "*.txt")
        
        print("\n📁 File Explorer demo completed!")
        print("Check your Desktop for new folder and file!")
        
    except Exception as e:
        print(f"❌ File Explorer demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(file_explorer_demo()) 