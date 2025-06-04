# Terminator SDK Test Project

A comprehensive project to test and explore the Terminator Python SDK for desktop automation with fun examples and advanced workflows!

## 🚀 Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the interactive playground:
```bash
python play_menu.py
```

## 🎮 Playground Scripts

### 🎪 Interactive Menu
- **`play_menu.py`** - Interactive menu to choose automation demos

### 🎨 Fun Automation Scripts
- **`play_paint.py`** - Automate MS Paint to create digital art
- **`play_file_explorer.py`** - Navigate folders and organize files  
- **`play_advanced_calc.py`** - Advanced calculator with scientific functions
- **`play_workflow.py`** - Multi-app workflows combining multiple applications

### 📝 Basic Examples
- **`example.py`** - Simple demo for beginners
- **`test_final.py`** - Comprehensive working test suite

### 🧪 Test Scripts
- **`test_basic.py`** - Basic functionality test
- **`test_working.py`** - Simple working example
- **`test_async.py`** - Async version test
- **`run_all_tests.py`** - Master test runner

## ✅ Working Example

The key to using Terminator SDK is wrapping your code in an asyncio event loop:

```python
import asyncio
import terminator

async def main():
    desktop = terminator.Desktop()
    desktop.open_application('calc')
    await asyncio.sleep(2)  # Wait for app to load
    
    seven = desktop.locator('name:Seven')
    seven.click()

asyncio.run(main())
```

## 🔧 Important Notes

- **Event Loop Required**: The SDK requires an asyncio event loop to be running, even though the methods aren't async
- **Package Name**: Install with `terminator-py` (not just `terminator`)
- **Version Tested**: terminator-py 0.3.7
- **Windows Support**: Designed primarily for Windows desktop automation

## 🎯 Features Demonstrated

### ✅ **Basic Desktop Automation**
- Desktop instance creation
- Application launching (`calc`, `notepad`, `mspaint`, `explorer`)
- Element location and clicking
- Text input and form filling

### ✅ **Advanced Automation**
- Multi-application workflows
- Scientific calculator functions
- Memory operations
- Paint tool selection and drawing
- File system navigation
- Real-time documentation generation

### ✅ **Creative Workflows**
- Art creation in Paint with automated documentation
- Calculator results → Notepad reporting
- File organization with summary generation
- Cross-application data transfer

## 🔍 Selector Patterns

The SDK supports various selector patterns for finding elements:

```python
# By name
desktop.locator('name:Seven')

# By role  
desktop.locator('role:Button')

# By automation ID
desktop.locator('automationid:CalculatorResults')

# By window title
desktop.locator('window:Calculator')

# Chained selectors
desktop.locator('window:Calculator').locator('name:Seven')
```

## 🎨 Fun Examples

### Paint Automation
```python
# Select brush and draw
brush = desktop.locator('name:Brush')
brush.click()

red = desktop.locator('name:Red')
red.click()

canvas = desktop.locator('window:Paint')
canvas.click()  # Draw!
```

### Advanced Calculator
```python
# Scientific mode
menu = desktop.locator('name:Menu')
menu.click()
scientific = desktop.locator('name:Scientific')
scientific.click()

# Square root of 16
desktop.locator('name:1').click()
desktop.locator('name:6').click()
desktop.locator('name:Square root').click()
```

### Multi-App Workflow
```python
# Calculate in calculator
desktop.open_application('calc')
# ... perform calculations ...

# Document in notepad
desktop.open_application('notepad')
editor = desktop.locator('name:Edit')
editor.type_text("Calculation results: ...")
```

## 🛠️ Troubleshooting

- **"no running event loop" error**: Wrap your code in `asyncio.run()` or run within an async function
- **Element not found**: Use Windows Accessibility Insights or FlaUInspect to find correct element names
- **App launch delays**: Add `await asyncio.sleep(2)` after opening applications
- **Paint/Explorer issues**: Element names may vary by Windows version

## 🎪 What's Included

- **8 different automation scripts** showcasing various capabilities
- **Interactive menu system** for easy exploration
- **Comprehensive test suite** for validation
- **Real-world workflow examples** 
- **Creative automation demos** (art, calculations, file management)
- **Multi-application coordination** examples

## 🚀 Next Steps

1. Run `python play_menu.py` to explore all demos
2. Try modifying the scripts to automate your own workflows
3. Explore other Windows applications
4. Create your own custom automation scripts
5. Combine multiple applications for complex workflows

## 📚 Documentation

- [Terminator Python SDK Reference](https://docs.screenpi.pe/terminator/python-sdk-reference)
- [GitHub Repository](https://github.com/mediar-ai/terminator)

---

**Have fun automating! 🤖✨** 