#!/usr/bin/env python3
"""
Master test runner for Terminator SDK
Runs all test scripts in sequence and provides summary
"""

import subprocess
import sys
import time

def run_test_script(script_name):
    """Run a test script and return success status"""
    try:
        print(f"\n{'='*50}")
        print(f"Running: {script_name}")
        print(f"{'='*50}")
        
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=False, 
                              text=True)
        
        success = result.returncode == 0
        print(f"\n{script_name} completed with return code: {result.returncode}")
        return success
        
    except Exception as e:
        print(f"Failed to run {script_name}: {e}")
        return False

def main():
    """Run all test scripts"""
    print("🚀 Terminator SDK - Complete Test Suite")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    test_scripts = [
        "test_basic.py",
        "test_calculator.py", 
        "test_notepad.py",
        "test_advanced.py"
    ]
    
    results = []
    
    for script in test_scripts:
        success = run_test_script(script)
        results.append((script, success))
        
        # Small delay between tests
        time.sleep(1)
    
    # Final summary
    print(f"\n{'='*60}")
    print("🏁 FINAL TEST SUMMARY")
    print(f"{'='*60}")
    
    passed = 0
    for script, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {script}")
        if success:
            passed += 1
    
    total = len(results)
    print(f"\nResults: {passed}/{total} test scripts passed")
    print(f"Completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Terminator SDK is working correctly.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test scripts failed. Check logs above for details.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 