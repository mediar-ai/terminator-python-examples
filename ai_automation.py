#!/usr/bin/env python3
"""
AI-Powered Automation with Ollama + LangChain + Terminator SDK
Uses AI to generate and execute desktop automation tasks
"""

import asyncio
import terminator
import json
import re
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser

class AutomationTaskParser(BaseOutputParser):
    """Parse AI responses into automation tasks"""
    
    def parse(self, text: str):
        """Parse the AI response into structured tasks"""
        try:
            # Try to extract JSON if present
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            
            # Fallback to text parsing
            return {"task": "text_generation", "content": text.strip()}
        except:
            return {"task": "text_generation", "content": text.strip()}

class AIAutomationAgent:
    """AI agent that generates and executes automation tasks"""
    
    def __init__(self, model_name="llama3.2"):
        """Initialize the AI agent"""
        print(f"🤖 Initializing AI Agent with model: {model_name}")
        self.llm = OllamaLLM(model=model_name)
        self.parser = AutomationTaskParser()
        self.desktop = terminator.Desktop()
        
    async def generate_calculator_tasks(self):
        """Have AI generate calculator problems to solve"""
        prompt = PromptTemplate.from_template("""
You are an AI assistant that generates interesting calculator problems.
Create 3 different calculator problems that would be fun to automate:
- One basic arithmetic (addition, subtraction, multiplication, division)
- One that uses parentheses for order of operations
- One with decimal numbers

Return your response as JSON with this format:
{{
    "problems": [
        {{"expression": "15*7", "description": "Basic multiplication"}},
        {{"expression": "100-(25+15)", "description": "Order of operations"}},
        {{"expression": "3.14*5", "description": "Decimal calculation"}}
    ]
}}

Only return the JSON, no other text.
        """)
        
        print("🧮 AI is generating calculator problems...")
        response = self.llm.invoke(prompt.format())
        tasks = self.parser.parse(response)
        
        if "problems" in tasks:
            return tasks["problems"]
        else:
            # Fallback problems if AI response parsing fails
            return [
                {"expression": "42+58", "description": "Simple addition"},
                {"expression": "10*9", "description": "Basic multiplication"},
                {"expression": "144/12", "description": "Division problem"}
            ]
    
    async def execute_calculator_automation(self, problems):
        """Execute calculator automation with AI-generated problems"""
        print("🔢 Executing AI-generated calculator tasks...")
        
        self.desktop.open_application('calc')
        await asyncio.sleep(2)
        
        results = []
        
        for i, problem in enumerate(problems, 1):
            print(f"  Problem {i}: {problem['description']} = {problem['expression']}")
            
            # Clear calculator
            try:
                clear_btn = self.desktop.locator('name:Clear')
                clear_btn.click()
                await asyncio.sleep(0.3)
            except:
                pass
            
            # Input the expression
            expression = problem['expression']
            for char in expression:
                if char.isdigit():
                    btn = self.desktop.locator(f'name:{char}')
                    btn.click()
                elif char == '+':
                    btn = self.desktop.locator('name:Plus')
                    btn.click()
                elif char == '-':
                    btn = self.desktop.locator('name:Minus')
                    btn.click()
                elif char == '*':
                    btn = self.desktop.locator('name:Multiply by')
                    btn.click()
                elif char == '/':
                    btn = self.desktop.locator('name:Divide by')
                    btn.click()
                elif char == '.':
                    btn = self.desktop.locator('name:Decimal separator')
                    btn.click()
                elif char == '(':
                    btn = self.desktop.locator('name:Open parenthesis')
                    btn.click()
                elif char == ')':
                    btn = self.desktop.locator('name:Close parenthesis')
                    btn.click()
                
                await asyncio.sleep(0.2)
            
            # Get result
            equals_btn = self.desktop.locator('name:Equals')
            equals_btn.click()
            await asyncio.sleep(0.5)
            
            results.append(problem)
            print(f"  ✓ Completed: {problem['expression']}")
        
        return results
    
    async def generate_creative_content(self):
        """Have AI generate creative content for notepad"""
        prompt = PromptTemplate.from_template("""
You are a creative AI assistant. Generate a fun, short story or poem (max 200 words) 
about a robot that learns to automate desktop computers. 
Make it whimsical and include some technical terms.
The story should be suitable for displaying in a text editor.
        """)
        
        print("📝 AI is generating creative content...")
        response = self.llm.invoke(prompt.format())
        return response.strip()
    
    async def execute_notepad_automation(self, content):
        """Execute notepad automation with AI-generated content"""
        print("📄 Creating AI-generated document in Notepad...")
        
        self.desktop.open_application('notepad')
        await asyncio.sleep(2)
        
        editor = self.desktop.locator('name:Edit')
        
        # Create a formatted document
        document = f"""AI-Generated Content Demo
Generated by Ollama + LangChain + Terminator SDK
{'='*50}

{content}

{'='*50}
Technical Details:
- AI Model: Local Ollama instance
- Framework: LangChain for prompt management
- Automation: Terminator SDK for desktop control
- Generated at: {__import__('time').strftime('%Y-%m-%d %H:%M:%S')}

This document was created entirely through AI-powered automation! 🤖✨
"""
        
        editor.type_text(document)
        print("✓ AI-generated content written to Notepad")
        
        return document
    
    async def generate_workflow_plan(self):
        """Have AI generate a workflow automation plan"""
        prompt = PromptTemplate.from_template("""
You are an AI automation expert. Create a simple 3-step workflow plan 
for desktop automation that involves calculator and notepad.

Return as JSON:
{{
    "workflow_name": "Name of the workflow",
    "description": "Brief description",
    "steps": [
        {{"step": 1, "action": "open_calculator", "description": "What to do"}},
        {{"step": 2, "action": "calculate", "expression": "math problem", "description": "Calculate something"}},
        {{"step": 3, "action": "document", "content": "what to write", "description": "Document the result"}}
    ]
}}

Make it creative but practical. Only return JSON.
        """)
        
        print("🔄 AI is planning automation workflow...")
        response = self.llm.invoke(prompt.format())
        workflow = self.parser.parse(response)
        
        # Fallback workflow if parsing fails
        if "workflow_name" not in workflow:
            workflow = {
                "workflow_name": "Daily Math & Documentation",
                "description": "Calculate daily expenses and document them",
                "steps": [
                    {"step": 1, "action": "open_calculator", "description": "Launch calculator app"},
                    {"step": 2, "action": "calculate", "expression": "25+15+30", "description": "Calculate total expenses"},
                    {"step": 3, "action": "document", "content": "Today's total expenses calculated", "description": "Document the calculation"}
                ]
            }
        
        return workflow
    
    async def execute_workflow(self, workflow):
        """Execute an AI-generated workflow"""
        print(f"🚀 Executing AI workflow: {workflow['workflow_name']}")
        print(f"Description: {workflow['description']}")
        
        results = []
        
        for step in workflow['steps']:
            print(f"\n📋 Step {step['step']}: {step['description']}")
            
            if step['action'] == 'open_calculator':
                self.desktop.open_application('calc')
                await asyncio.sleep(2)
                results.append("Calculator opened")
                
            elif step['action'] == 'calculate':
                # Clear and calculate
                try:
                    clear_btn = self.desktop.locator('name:Clear')
                    clear_btn.click()
                    await asyncio.sleep(0.3)
                except:
                    pass
                
                expression = step.get('expression', '1+1')
                print(f"   Calculating: {expression}")
                
                for char in expression:
                    if char.isdigit():
                        btn = self.desktop.locator(f'name:{char}')
                        btn.click()
                    elif char == '+':
                        btn = self.desktop.locator('name:Plus')
                        btn.click()
                    elif char == '-':
                        btn = self.desktop.locator('name:Minus')
                        btn.click()
                    elif char == '*':
                        btn = self.desktop.locator('name:Multiply by')
                        btn.click()
                    elif char == '/':
                        btn = self.desktop.locator('name:Divide by')
                        btn.click()
                    await asyncio.sleep(0.2)
                
                equals_btn = self.desktop.locator('name:Equals')
                equals_btn.click()
                await asyncio.sleep(0.5)
                results.append(f"Calculated: {expression}")
                
            elif step['action'] == 'document':
                self.desktop.open_application('notepad')
                await asyncio.sleep(2)
                
                editor = self.desktop.locator('name:Edit')
                
                workflow_doc = f"""AI Workflow Execution Report
{workflow['workflow_name']}
{'='*40}

Workflow Description:
{workflow['description']}

Execution Results:
"""
                for i, result in enumerate(results, 1):
                    workflow_doc += f"{i}. {result}\n"
                
                workflow_doc += f"""
{step.get('content', 'Workflow completed successfully!')}

Generated by AI-powered automation system
Timestamp: {__import__('time').strftime('%Y-%m-%d %H:%M:%S')}
"""
                
                editor.type_text(workflow_doc)
                results.append("Workflow documented")
            
            print(f"   ✓ Step completed")
        
        print(f"\n🎉 Workflow '{workflow['workflow_name']}' completed successfully!")
        return results

async def main():
    """Main AI automation demo"""
    print("🤖 AI-POWERED DESKTOP AUTOMATION DEMO")
    print("="*60)
    print("Combining Ollama + LangChain + Terminator SDK")
    print("="*60)
    
    try:
        # Initialize AI agent
        agent = AIAutomationAgent()
        
        print("\n🎯 Demo 1: AI-Generated Calculator Problems")
        print("-" * 50)
        problems = await agent.generate_calculator_tasks()
        await agent.execute_calculator_automation(problems)
        
        await asyncio.sleep(2)
        
        print("\n🎯 Demo 2: AI-Generated Creative Content")
        print("-" * 50)
        content = await agent.generate_creative_content()
        await agent.execute_notepad_automation(content)
        
        await asyncio.sleep(2)
        
        print("\n🎯 Demo 3: AI-Planned Automation Workflow")
        print("-" * 50)
        workflow = await agent.generate_workflow_plan()
        await agent.execute_workflow(workflow)
        
        print("\n" + "="*60)
        print("🎊 AI-POWERED AUTOMATION DEMO COMPLETED!")
        print("="*60)
        print("\nWhat just happened:")
        print("• AI generated calculator problems and we solved them")
        print("• AI wrote creative content and we typed it in Notepad")
        print("• AI planned and executed a complete workflow")
        print("• All desktop interactions were automated!")
        print("\nThis is the future of intelligent automation! 🚀")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        print("\nMake sure you have:")
        print("1. Ollama installed and running (ollama serve)")
        print("2. A model pulled (ollama pull llama3.2)")
        print("3. All Python dependencies installed")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main()) 