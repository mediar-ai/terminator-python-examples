#!/usr/bin/env python3
"""
Latest AI Models Test - Testing newest Ollama models
Tests Llama 3.3, Gemma2, DeepSeek, Qwen2.5, and other cutting-edge models
"""

import asyncio
import terminator
import ollama
import time

class LatestModelTester:
    """Test the newest AI models with desktop automation"""
    
    def __init__(self):
        """Initialize the tester"""
        self.desktop = terminator.Desktop()
        
        # Latest models to test (in order of preference)
        self.models_to_test = [
            "deepseek-r1:1.5b",    # Latest DeepSeek-R1 model (user requested)
        ]
        
        self.available_models = []
        
    async def check_available_models(self):
        """Check which models are available"""
        print("🔍 Checking available models...")
        
        try:
            models = ollama.list()
            print(f"✓ Found {len(models.get('models', []))} installed models")
            
            # Get model names properly
            available_names = []
            for model in models.get('models', []):
                if isinstance(model, dict) and 'name' in model:
                    available_names.append(model['name'])
                elif isinstance(model, str):
                    available_names.append(model)
            
            print(f"Available models: {available_names}")
            
            # Find which of our preferred models are available
            for model in self.models_to_test:
                found = False
                for available in available_names:
                    if model in available or available.startswith(model):
                        self.available_models.append(model)
                        print(f"  ✅ {model} - Available (as {available})")
                        found = True
                        break
                
                if not found:
                    print(f"  ❌ {model} - Not installed")
            
            if not self.available_models:
                print("⚠️ No preferred models found. Will try to use any available model...")
                # Fallback: use any available model
                if available_names:
                    self.available_models = available_names[:3]  # Use first 3 available
                    print(f"Using available models: {self.available_models}")
                    return True
                return False
                
            return True
            
        except Exception as e:
            print(f"❌ Failed to check models: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    async def download_latest_model(self):
        """Download the latest recommended model"""
        recommended_models = ["deepseek-r1:1.5b"]
        
        for model in recommended_models:
            try:
                print(f"📥 Attempting to download {model}...")
                # Note: This would require running ollama pull in terminal
                print(f"To download {model}, run: ollama pull {model}")
                return model
            except Exception as e:
                print(f"Failed to download {model}: {e}")
                continue
        
        return None
    
    async def test_model_creativity(self, model_name):
        """Test a model's creative writing abilities"""
        print(f"\n🎨 Testing {model_name} - Creative Writing")
        print("-" * 50)
        
        try:
            start_time = time.time()
            
            prompt = """Write a very short (max 100 words), creative story about an AI that discovers it can control desktop applications. Make it fun and mention specific apps like Calculator and Notepad. Be creative but concise."""
            
            response = ollama.chat(model=model_name, messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            response_time = time.time() - start_time
            content = response['message']['content']
            
            print(f"⏱️ Response time: {response_time:.2f}s")
            print(f"📝 Content length: {len(content)} characters")
            print(f"✨ Generated content preview:")
            print("-" * 30)
            print(content[:200] + "..." if len(content) > 200 else content)
            print("-" * 30)
            
            return {
                'model': model_name,
                'task': 'creative_writing',
                'response_time': response_time,
                'content_length': len(content),
                'content': content,
                'success': True
            }
            
        except Exception as e:
            print(f"❌ Creative test failed for {model_name}: {e}")
            return {
                'model': model_name,
                'task': 'creative_writing',
                'success': False,
                'error': str(e)
            }
    
    async def test_model_math_generation(self, model_name):
        """Test a model's ability to generate math problems"""
        print(f"\n🧮 Testing {model_name} - Math Problem Generation")
        print("-" * 50)
        
        try:
            start_time = time.time()
            
            prompt = """Generate exactly 3 calculator problems. Return ONLY the math expressions, one per line. Examples:
25*4
100-37
15+28
Make them interesting but simple enough for a basic calculator."""
            
            response = ollama.chat(model=model_name, messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            response_time = time.time() - start_time
            content = response['message']['content']
            
            # Extract math expressions
            import re
            expressions = re.findall(r'\d+[\+\-\*/]\d+', content)
            
            print(f"⏱️ Response time: {response_time:.2f}s")
            print(f"🔢 Found {len(expressions)} math expressions")
            print(f"📊 Expressions: {expressions}")
            
            return {
                'model': model_name,
                'task': 'math_generation',
                'response_time': response_time,
                'expressions': expressions,
                'raw_content': content,
                'success': len(expressions) > 0
            }
            
        except Exception as e:
            print(f"❌ Math test failed for {model_name}: {e}")
            return {
                'model': model_name,
                'task': 'math_generation',
                'success': False,
                'error': str(e)
            }
    
    async def test_model_automation_planning(self, model_name):
        """Test a model's ability to plan automation workflows"""
        print(f"\n🤖 Testing {model_name} - Automation Planning")
        print("-" * 50)
        
        try:
            start_time = time.time()
            
            prompt = """Plan a 3-step desktop automation workflow. Be specific about applications and actions. Format as:
Step 1: [Action]
Step 2: [Action] 
Step 3: [Action]

Example:
Step 1: Open Calculator app
Step 2: Calculate 50+25
Step 3: Open Notepad and document the result

Make it practical and specific."""
            
            response = ollama.chat(model=model_name, messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            response_time = time.time() - start_time
            content = response['message']['content']
            
            # Extract steps
            steps = re.findall(r'Step \d+:.*', content)
            
            print(f"⏱️ Response time: {response_time:.2f}s")
            print(f"📋 Found {len(steps)} workflow steps")
            print("🎯 Workflow plan:")
            for step in steps:
                print(f"  {step}")
            
            return {
                'model': model_name,
                'task': 'automation_planning',
                'response_time': response_time,
                'steps': steps,
                'raw_content': content,
                'success': len(steps) >= 3
            }
            
        except Exception as e:
            print(f"❌ Planning test failed for {model_name}: {e}")
            return {
                'model': model_name,
                'task': 'automation_planning',
                'success': False,
                'error': str(e)
            }
    
    async def demonstrate_best_model(self, best_model, test_results):
        """Demonstrate the best performing model with actual automation"""
        print(f"\n🌟 DEMONSTRATING BEST MODEL: {best_model}")
        print("="*60)
        
        try:
            # Generate content with the best model
            print("🧠 Generating automation content...")
            
            response = ollama.chat(model=best_model, messages=[
                {'role': 'user', 'content': 'Write a short message (max 100 words) celebrating the successful testing of AI models for desktop automation. Mention specific models tested and be enthusiastic!'}
            ])
            
            content = response['message']['content']
            
            # Automate Notepad to display the content
            print("📝 Automating Notepad to display results...")
            
            self.desktop.open_application('notepad')
            await asyncio.sleep(2)
            
            editor = self.desktop.locator('name:Edit')
            
            # Create a comprehensive report
            report = f"""🤖 LATEST AI MODELS TEST RESULTS
{'='*50}
Test Date: {time.strftime('%Y-%m-%d %H:%M:%S')}
Best Performing Model: {best_model}

AI-GENERATED CELEBRATION MESSAGE:
{content}

{'='*50}
MODELS TESTED:
"""
            
            for result in test_results:
                if result['success']:
                    report += f"✅ {result['model']} - {result['task']} ({result['response_time']:.2f}s)\n"
                else:
                    report += f"❌ {result['model']} - {result['task']} (Failed)\n"
            
            report += f"""
{'='*50}
TECHNOLOGY STACK:
- AI Models: Latest Ollama models
- Desktop Automation: Terminator SDK
- Integration: Python asyncio
- Local Processing: No cloud dependencies

This report was generated entirely by AI and typed automatically! 🚀
"""
            
            editor.type_text(report)
            print("✅ Automation demonstration completed!")
            
            return True
            
        except Exception as e:
            print(f"❌ Demonstration failed: {e}")
            return False
    
    async def run_comprehensive_test(self):
        """Run comprehensive tests on all available models"""
        print("🚀 LATEST AI MODELS COMPREHENSIVE TEST")
        print("="*60)
        print("Testing cutting-edge models with desktop automation")
        print("="*60)
        
        # Check available models
        if not await self.check_available_models():
            print("\n⚠️ No preferred models available.")
            print("Please install models with:")
            print("ollama pull llama3.3")
            print("ollama pull gemma2:9b") 
            print("ollama pull qwen2.5:7b")
            return
        
        print(f"\n🎯 Testing {len(self.available_models)} models...")
        
        all_results = []
        model_scores = {}
        
        # Test each available model
        for model in self.available_models[:3]:  # Limit to top 3 for demo
            print(f"\n{'='*60}")
            print(f"🔬 TESTING MODEL: {model}")
            print(f"{'='*60}")
            
            # Run all tests for this model
            results = []
            results.append(await self.test_model_creativity(model))
            results.append(await self.test_model_math_generation(model))
            results.append(await self.test_model_automation_planning(model))
            
            # Calculate score for this model
            successful_tests = sum(1 for r in results if r['success'])
            avg_response_time = sum(r.get('response_time', 10) for r in results if r['success']) / max(successful_tests, 1)
            
            model_scores[model] = {
                'successful_tests': successful_tests,
                'avg_response_time': avg_response_time,
                'score': successful_tests * 10 - avg_response_time  # Higher is better
            }
            
            all_results.extend(results)
            
            print(f"\n📊 {model} Summary:")
            print(f"  ✅ Successful tests: {successful_tests}/3")
            print(f"  ⏱️ Average response time: {avg_response_time:.2f}s")
            print(f"  🏆 Score: {model_scores[model]['score']:.2f}")
        
        # Find the best model
        if model_scores:
            best_model = max(model_scores.keys(), key=lambda x: model_scores[x]['score'])
            
            print(f"\n🏆 BEST PERFORMING MODEL: {best_model}")
            print(f"Score: {model_scores[best_model]['score']:.2f}")
            
            # Demonstrate the best model
            await self.demonstrate_best_model(best_model, all_results)
            
        print(f"\n{'='*60}")
        print("🎊 COMPREHENSIVE TEST COMPLETED!")
        print(f"{'='*60}")
        print("Latest AI models successfully tested with desktop automation!")
        print("Check your Notepad for the full test results! 📝")

async def main():
    """Main test function"""
    tester = LatestModelTester()
    await tester.run_comprehensive_test()

if __name__ == "__main__":
    asyncio.run(main()) 