# Terminator SDK Test Project

A comprehensive project to test and explore the Terminator Python SDK for desktop automation with fun examples, advanced workflows, and **AI-powered automation**!

## 🚀 Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. For AI features, install and start Ollama:
```bash
# Install Ollama (see AI_SETUP.md for details)
ollama serve
ollama pull llama3.2
```

3. Run the interactive playground:
```bash
python play_menu.py
```

## 🎮 Playground Scripts

### 🎪 Interactive Menu
- **`play_menu.py`** - Interactive menu to choose automation demos (now with AI options!)

### 🎨 Basic Automation Scripts
- **`play_paint.py`** - Automate MS Paint to create digital art
- **`play_file_explorer.py`** - Navigate folders and organize files  
- **`play_advanced_calc.py`** - Advanced calculator with scientific functions
- **`play_workflow.py`** - Multi-app workflows combining multiple applications

### 🤖 AI-Powered Automation Scripts
- **`ai_simple.py`** - Beginner-friendly AI automation (AI stories + calculator help)
- **`ai_automation.py`** - Advanced AI agent with smart workflow planning
- **`AI_SETUP.md`** - Complete setup guide for AI features

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

## 🤖 AI-Powered Automation Example

Combine AI with desktop automation for intelligent workflows:

```python
import asyncio
import ollama
import terminator

async def ai_automation():
    # 1. AI generates content
    response = ollama.chat(model='llama3.2', messages=[
        {'role': 'user', 'content': 'Write a fun story about robots'}
    ])
    
    # 2. Automate desktop to use the content
    desktop = terminator.Desktop()
    desktop.open_application('notepad')
    await asyncio.sleep(2)
    
    editor = desktop.locator('name:Edit')
    editor.type_text(response['message']['content'])

asyncio.run(ai_automation())
```

## 🔧 Important Notes

- **Event Loop Required**: The SDK requires an asyncio event loop to be running, even though the methods aren't async
- **Package Name**: Install with `terminator-py` (not just `terminator`)
- **Version Tested**: terminator-py 0.3.7
- **Windows Support**: Designed primarily for Windows desktop automation
- **AI Features**: Requires Ollama for local AI models (see `AI_SETUP.md`)

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

### 🤖 **AI-Powered Automation**
- AI content generation → automated typing
- Intelligent task planning and execution
- Dynamic workflow creation
- AI-suggested automation sequences
- Smart problem-solving assistance

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

### AI-Generated Calculator Tasks
```python
# AI suggests math problems
prompt = "Give me 3 calculator problems to solve"
response = ollama.chat(model='llama3.2', messages=[
    {'role': 'user', 'content': prompt}
])

# Parse and execute automatically
expressions = extract_math_expressions(response['message']['content'])
for expr in expressions:
    await calculate_expression(desktop, expr)
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

### Basic Automation Issues
- **"no running event loop" error**: Wrap your code in `asyncio.run()` or run within an async function
- **Element not found**: Use Windows Accessibility Insights or FlaUInspect to find correct element names
- **App launch delays**: Add `await asyncio.sleep(2)` after opening applications
- **Paint/Explorer issues**: Element names may vary by Windows version

### AI Automation Issues
- **"Connection refused"**: Make sure `ollama serve` is running
- **"Model not found"**: Run `ollama pull llama3.2` to download models
- **Slow AI responses**: Try smaller models like `llama3.2:1b`
- **Import errors**: Install with `pip install ollama langchain langchain-ollama`

## 🎪 What's Included

- **8+ automation scripts** showcasing various capabilities
- **2 AI-powered automation demos** with intelligent task generation
- **Interactive menu system** for easy exploration
- **Comprehensive test suite** for validation
- **Real-world workflow examples** 
- **Creative automation demos** (art, calculations, file management)
- **Multi-application coordination** examples
- **AI integration examples** for intelligent automation

## 🚀 Next Steps

### Basic Automation
1. Run `python play_menu.py` to explore all demos
2. Try modifying the scripts to automate your own workflows
3. Explore other Windows applications
4. Create your own custom automation scripts

### AI-Powered Automation
1. Set up Ollama following `AI_SETUP.md`
2. Run `python ai_simple.py` for your first AI automation
3. Try `python ai_automation.py` for advanced AI workflows
4. Experiment with different AI models and prompts
5. Create your own AI automation agents

### Advanced Development
1. Combine multiple applications for complex workflows
2. Build AI agents that plan and execute automation tasks
3. Create intelligent assistants for daily computer tasks
4. Explore integration with other AI services and APIs

## 📚 Documentation

- [Terminator Python SDK Reference](https://docs.screenpi.pe/terminator/python-sdk-reference)
- [GitHub Repository](https://github.com/mediar-ai/terminator)
- [Ollama Documentation](https://ollama.ai/docs)
- [LangChain Documentation](https://python.langchain.com/)

## 🌟 Technology Stack

- **Desktop Automation**: Terminator SDK
- **AI/LLM**: Ollama (local models)
- **AI Framework**: LangChain
- **Async Support**: Python asyncio
- **Models Tested**: Llama 3.2, Llama 3, Qwen2

---

**Welcome to the future of intelligent desktop automation! 🤖✨** 

This project demonstrates how AI can be seamlessly integrated with desktop automation to create intelligent, adaptive workflows that can understand, plan, and execute complex tasks autonomously. 