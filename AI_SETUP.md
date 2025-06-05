# AI-Powered Automation Setup Guide

This guide will help you set up AI-powered desktop automation using Ollama + LangChain + Terminator SDK.

## 🚀 Quick Setup

### 1. Install Ollama

**Windows:**
- Download from: https://ollama.ai/download
- Run the installer
- Or use: `winget install Ollama.Ollama`

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. Start Ollama Service

```bash
ollama serve
```

### 3. Download a Model

```bash
# Recommended for most users (lightweight)
ollama pull llama3.2

# Alternative models
ollama pull llama3.2:1b    # Even smaller/faster
ollama pull llama3:8b      # Larger/more capable
ollama pull qwen2:7b       # Good alternative
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

The requirements.txt should now include:
- `terminator-py` - Desktop automation
- `ollama` - Ollama Python client
- `langchain` - AI framework
- `langchain-ollama` - LangChain + Ollama integration

## 🧪 Test the Setup

### Simple Test
```bash
python ai_simple.py
```

### Advanced Test
```bash
python ai_automation.py
```

## 🎯 Available AI Demos

### 1. **`ai_simple.py`** - Beginner-Friendly
- AI generates creative stories
- Auto-types content in Notepad
- AI suggests calculator problems
- Simple and easy to understand

### 2. **`ai_automation.py`** - Advanced Features
- Structured AI task generation
- Complex workflow planning
- Multi-step automation sequences
- JSON-based AI responses

## 🛠️ How It Works

```python
import ollama
import terminator

# 1. AI generates content
response = ollama.chat(model='llama3.2', messages=[
    {'role': 'user', 'content': 'Write a fun story about robots'}
])

# 2. Extract the content
content = response['message']['content']

# 3. Automate desktop to use the content
desktop = terminator.Desktop()
desktop.open_application('notepad')
editor = desktop.locator('name:Edit')
editor.type_text(content)
```

## 🎨 Example Use Cases

### Creative Automation
- AI writes stories/poems → Auto-typed in documents
- AI generates art descriptions → Paint automation
- AI creates todo lists → File organization

### Smart Workflows
- AI plans calculation sequences → Calculator automation
- AI generates test data → Form filling
- AI creates documentation → Report generation

### Intelligent Assistance
- AI suggests optimizations → System automation
- AI generates scripts → Code automation
- AI plans schedules → Calendar automation

## 🔧 Troubleshooting

### Common Issues

**"Connection refused" or "Ollama not found"**
- Make sure `ollama serve` is running
- Check if Ollama is installed correctly
- Try restarting the Ollama service

**"Model not found"**
- Run `ollama pull llama3.2` to download the model
- Check available models: `ollama list`

**"Slow responses"**
- Try a smaller model: `ollama pull llama3.2:1b`
- Check system resources (RAM/CPU)
- Close other applications

**"LangChain import errors"**
- Install with: `pip install langchain langchain-ollama`
- Try updating: `pip install --upgrade langchain`

### Model Recommendations

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| `llama3.2:1b` | ~1GB | Fast | Good | Simple tasks, testing |
| `llama3.2` (3b) | ~2GB | Medium | Better | General use, recommended |
| `llama3:8b` | ~4.7GB | Slower | Best | Complex tasks, detailed output |

## 🌟 Advanced Configuration

### Custom Model Settings
```python
# In your scripts, you can customize:
response = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': prompt}],
    options={
        'temperature': 0.7,  # Creativity (0-1)
        'top_p': 0.9,       # Diversity
        'num_predict': 200   # Max response length
    }
)
```

### LangChain Integration
```python
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

llm = OllamaLLM(model="llama3.2")
prompt = PromptTemplate.from_template("Write a {type} about {topic}")
chain = prompt | llm
result = chain.invoke({"type": "story", "topic": "robots"})
```

## 🎉 Ready to Go!

Once set up, you can:

1. **Run the simple demo:** `python ai_simple.py`
2. **Try advanced automation:** `python ai_automation.py`
3. **Add to the playground menu:** Update `play_menu.py`
4. **Create your own AI automation scripts!**

The combination of AI + desktop automation opens up incredible possibilities for intelligent, adaptive workflows! 🤖✨

## 💡 Next Steps

- Experiment with different AI models
- Create custom automation agents
- Build complex multi-step workflows
- Integrate with other AI services
- Share your creations with the community!

Have fun building the future of intelligent automation! 🚀 