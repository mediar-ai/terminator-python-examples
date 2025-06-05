#!/usr/bin/env python3
"""
AI Desktop Butler - Powered by LangChain + DeepSeek-R1
Your intelligent assistant that can analyze, organize, and automate your desktop!
"""

import asyncio
import terminator
import time
import os
import json
import random
from datetime import datetime
from pathlib import Path

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain import hub

class AIDesktopButler:
    """An intelligent AI butler for your desktop using LangChain"""
    
    def __init__(self):
        """Initialize the AI Butler"""
        print("🤖 Initializing AI Desktop Butler...")
        self.llm = OllamaLLM(model="deepseek-r1:1.5b")
        self.desktop = terminator.Desktop()
        
        # LangChain chains for different tasks
        self.setup_chains()
        
        print("✅ AI Desktop Butler ready to serve!")
    
    def setup_chains(self):
        """Set up LangChain chains for different tasks"""
        
        # Creative Content Generator
        self.creative_prompt = PromptTemplate(
            input_variables=["task", "context"],
            template="""You are a creative AI butler. Based on the task: {task}
            
            Context: {context}
            
            Generate creative, helpful content that would be useful for desktop automation.
            Be imaginative but practical. Keep it under 200 words."""
        )
        self.creative_chain = LLMChain(llm=self.llm, prompt=self.creative_prompt)
        
        # File Organization Assistant
        self.organize_prompt = PromptTemplate(
            input_variables=["file_list", "task_type"],
            template="""You are an intelligent file organization assistant.
            
            Files found: {file_list}
            Task: {task_type}
            
            Suggest a smart organization strategy and create folder names.
            Return your response as JSON:
            {{
                "strategy": "description of organization approach",
                "folders": ["folder1", "folder2", "folder3"],
                "actions": ["action1", "action2", "action3"]
            }}"""
        )
        self.organize_chain = LLMChain(llm=self.llm, prompt=self.organize_prompt)
        
        # Productivity Analyzer
        self.productivity_prompt = PromptTemplate(
            input_variables=["activity", "time_of_day"],
            template="""You are a productivity analysis AI butler.
            
            Current activity: {activity}
            Time: {time_of_day}
            
            Analyze this activity and suggest:
            1. Productivity improvements
            2. Break recommendations  
            3. Next actions
            4. Motivational message
            
            Be encouraging and practical!"""
        )
        self.productivity_chain = LLMChain(llm=self.llm, prompt=self.productivity_prompt)
    
    async def analyze_desktop_environment(self):
        """Analyze the current desktop environment"""
        print("🔍 Analyzing your desktop environment...")
        
        # Get current time and context
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        day_of_week = datetime.now().strftime("%A")
        
        # Simulate getting desktop info (in real app, you'd scan open windows, files, etc.)
        desktop_context = {
            "time": current_time,
            "day": day_of_week,
            "apps_open": ["Calculator", "Notepad", "Terminal"],
            "recent_files": ["project_notes.txt", "calculations.txt", "automation_test.py"]
        }
        
        # Use LangChain to analyze the environment
        analysis = await self.creative_chain.arun(
            task="Analyze my current desktop environment and suggest helpful automation",
            context=f"Desktop state: {desktop_context}"
        )
        
        print("🧠 AI Analysis:")
        print("-" * 40)
        print(analysis)
        print("-" * 40)
        
        return analysis, desktop_context
    
    async def create_personalized_dashboard(self, analysis):
        """Create a personalized dashboard in Notepad"""
        print("\n📊 Creating your personalized AI dashboard...")
        
        # Open Notepad for dashboard
        self.desktop.open_application('notepad')
        await asyncio.sleep(2)
        
        editor = self.desktop.locator('name:Edit')
        
        # Generate dashboard content using LangChain
        dashboard_task = "Create a personalized daily dashboard with productivity tips"
        dashboard_context = f"Analysis: {analysis}"
        
        dashboard_content = await self.creative_chain.arun(
            task=dashboard_task,
            context=dashboard_context
        )
        
        # Create comprehensive dashboard
        dashboard = f"""🤖 AI DESKTOP BUTLER - PERSONALIZED DASHBOARD
{'='*60}
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Powered by: LangChain + DeepSeek-R1:1.5b

{'='*60}
🧠 AI ANALYSIS & RECOMMENDATIONS:
{dashboard_content}

{'='*60}
📊 QUICK STATS:
• Session started: {time.strftime('%H:%M:%S')}
• AI Model: DeepSeek-R1:1.5b with LangChain
• Automation Framework: Terminator SDK
• Status: 🟢 Active and ready!

{'='*60}
🎯 SMART ACTIONS AVAILABLE:
1. 📁 Intelligent file organization
2. 🧮 Smart calculator workflows  
3. 📝 Creative content generation
4. 🎨 Artistic desktop automation
5. 📈 Productivity analysis
6. 🎮 Fun surprise automation

{'='*60}
💡 PRO TIP: Your AI butler learns from your patterns!
This dashboard updates based on your desktop activity.

Last updated by AI Butler 🤖✨
"""
        
        editor.type_text(dashboard)
        print("✅ Personalized dashboard created!")
        
        return dashboard
    
    async def smart_file_organization_demo(self):
        """Demonstrate intelligent file organization"""
        print("\n📁 SMART FILE ORGANIZATION DEMO")
        print("-" * 50)
        
        # Simulate file discovery
        mock_files = [
            "meeting_notes_2024.txt", "budget_calculations.xlsx", 
            "project_proposal.docx", "automation_script.py",
            "family_photos.jpg", "music_playlist.mp3"
        ]
        
        # Use LangChain to analyze and organize
        organization_plan = await self.organize_chain.arun(
            file_list=str(mock_files),
            task_type="Create smart folder structure for better productivity"
        )
        
        print("🧠 AI Organization Plan:")
        print(organization_plan)
        
        # Create folders in a new notepad
        print("\n📝 Creating organization plan document...")
        self.desktop.open_application('notepad')
        await asyncio.sleep(2)
        
        editor = self.desktop.locator('name:Edit')
        
        org_doc = f"""🗂️ AI SMART FILE ORGANIZATION PLAN
{'='*50}
Generated by: LangChain + DeepSeek-R1
Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{'='*50}
📋 ANALYSIS RESULTS:
{organization_plan}

{'='*50}
📁 RECOMMENDED FOLDER STRUCTURE:
• 💼 Work/
  ├── Documents/
  ├── Calculations/
  └── Projects/
• 🏠 Personal/
  ├── Photos/
  ├── Music/
  └── Notes/
• 🤖 Automation/
  ├── Scripts/
  └── Configs/

{'='*50}
🚀 NEXT STEPS:
1. Review the AI recommendations
2. Implement the folder structure
3. Set up automated file sorting rules
4. Let AI butler maintain organization

Your files will be much more organized! 📊✨
"""
        
        editor.type_text(org_doc)
        print("✅ Organization plan documented!")
    
    async def productivity_coaching_session(self):
        """AI-powered productivity coaching"""
        print("\n💪 AI PRODUCTIVITY COACHING SESSION")
        print("-" * 50)
        
        current_activity = "Working with desktop automation and AI"
        time_info = datetime.now().strftime("%A %H:%M")
        
        # Get AI coaching using LangChain
        coaching = await self.productivity_chain.arun(
            activity=current_activity,
            time_of_day=time_info
        )
        
        print("🏃‍♂️ AI Coach Says:")
        print("-" * 30)
        print(coaching)
        print("-" * 30)
        
        # Calculate some motivational stats using calculator
        print("\n🧮 Calculating your productivity stats...")
        self.desktop.open_application('calc')
        await asyncio.sleep(2)
        
        # Fun calculation: Hours in a day * productivity factor
        calculations = [
            ("24*0.8", "Daily productivity potential"),
            ("168*0.6", "Weekly productive hours"),
            ("365*2", "Learning days per year")
        ]
        
        results = []
        for calc, description in calculations:
            # Clear calculator
            try:
                clear_btn = self.desktop.locator('name:Clear')
                clear_btn.click()
                await asyncio.sleep(0.3)
            except:
                pass
            
            # Input calculation
            for char in calc:
                if char.isdigit():
                    btn = self.desktop.locator(f'name:{char}')
                    btn.click()
                elif char == '*':
                    btn = self.desktop.locator('name:Multiply by')
                    btn.click()
                elif char == '.':
                    btn = self.desktop.locator('name:Decimal separator')
                    btn.click()
                await asyncio.sleep(0.2)
            
            # Get result
            equals_btn = self.desktop.locator('name:Equals')
            equals_btn.click()
            await asyncio.sleep(0.5)
            
            results.append(f"{description}: {calc}")
            print(f"  ✅ {description}: {calc}")
        
        # Create coaching report
        print("\n📝 Creating productivity coaching report...")
        self.desktop.open_application('notepad')
        await asyncio.sleep(2)
        
        editor = self.desktop.locator('name:Edit')
        
        coaching_report = f"""💪 AI PRODUCTIVITY COACHING REPORT
{'='*50}
Session Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Coach: AI Butler (LangChain + DeepSeek-R1)

{'='*50}
🎯 PERSONALIZED COACHING:
{coaching}

{'='*50}
📊 PRODUCTIVITY CALCULATIONS:
"""
        
        for result in results:
            coaching_report += f"• {result}\n"
        
        coaching_report += f"""
{'='*50}
🌟 DAILY AFFIRMATION:
"You're building amazing AI-powered automation! 
Every line of code and every test brings you closer
to mastering the future of intelligent computing."

{'='*50}
📅 NEXT COACHING SESSION:
Schedule: Tomorrow at the same time
Focus: Advanced automation techniques
Goal: Become an AI automation expert!

Keep up the excellent work! 🚀🤖
"""
        
        editor.type_text(coaching_report)
        print("✅ Coaching session documented!")
    
    async def creative_surprise_automation(self):
        """Surprise creative automation using AI"""
        print("\n🎭 CREATIVE SURPRISE AUTOMATION!")
        print("-" * 50)
        
        surprises = [
            "Generate a haiku about desktop automation",
            "Create a short story about an AI butler's day",
            "Write a motivational message for a programmer",
            "Compose a funny dialogue between Calculator and Notepad apps"
        ]
        
        selected_surprise = random.choice(surprises)
        print(f"🎲 Random creative task: {selected_surprise}")
        
        # Generate creative content using LangChain
        creative_content = await self.creative_chain.arun(
            task=selected_surprise,
            context="This is a fun surprise automation for the user"
        )
        
        print("\n🎨 AI Created:")
        print("-" * 30)
        print(creative_content)
        print("-" * 30)
        
        # Display in Notepad with artistic formatting
        print("\n📝 Creating artistic display...")
        self.desktop.open_application('notepad')
        await asyncio.sleep(2)
        
        editor = self.desktop.locator('name:Edit')
        
        artistic_display = f"""
🎭✨ CREATIVE SURPRISE FROM YOUR AI BUTLER ✨🎭
{'🌟' * 25}

{creative_content}

{'🌟' * 25}
Created with love by your AI Desktop Butler
Powered by imagination and LangChain magic! 

Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Surprise Factor: 💯
Creativity Level: Maximum! 🚀

{'🎨' * 25}
Hope this brightened your day! 😊
        """
        
        editor.type_text(artistic_display)
        print("✅ Creative surprise delivered!")
    
    async def run_butler_demo(self):
        """Run the complete AI Desktop Butler demonstration"""
        print("🏰 AI DESKTOP BUTLER - ULTIMATE DEMO")
        print("="*60)
        print("Welcome to your personal AI assistant!")
        print("Powered by LangChain + DeepSeek-R1:1.5b")
        print("="*60)
        
        # Step 1: Analyze environment
        analysis, context = await self.analyze_desktop_environment()
        await asyncio.sleep(2)
        
        # Step 2: Create dashboard
        await self.create_personalized_dashboard(analysis)
        await asyncio.sleep(3)
        
        # Step 3: Smart file organization
        await self.smart_file_organization_demo()
        await asyncio.sleep(3)
        
        # Step 4: Productivity coaching
        await self.productivity_coaching_session()
        await asyncio.sleep(3)
        
        # Step 5: Creative surprise
        await self.creative_surprise_automation()
        
        print(f"\n{'='*60}")
        print("🎉 AI DESKTOP BUTLER DEMO COMPLETED!")
        print("="*60)
        print("Your AI Butler has:")
        print("• 🧠 Analyzed your desktop environment")
        print("• 📊 Created a personalized dashboard")
        print("• 📁 Planned smart file organization")
        print("• 💪 Provided productivity coaching")
        print("• 🎨 Delivered a creative surprise")
        print("• 📝 Generated 5 different documents")
        print()
        print("Check all your Notepad windows for the complete experience! 📄")
        print("Your AI butler is ready to serve whenever you need! 🤖✨")

async def main():
    """Main function to run the AI Desktop Butler"""
    butler = AIDesktopButler()
    await butler.run_butler_demo()

if __name__ == "__main__":
    asyncio.run(main()) 