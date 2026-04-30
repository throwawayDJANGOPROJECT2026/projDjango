#!/usr/bin/env python
"""
Django development server runner - works on Windows, macOS, and Linux
Usage: python run_server.py
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def main():
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Determine Python executable path based on platform
    if platform.system() == "Windows":
        python_exe = project_dir / "venv" / "Scripts" / "python.exe"
    else:
        python_exe = project_dir / "venv" / "bin" / "python"
    
    # Check if venv exists
    if not python_exe.exists():
        print("❌ Virtual environment not found!")
        print("\nPlease run setup first:")
        if platform.system() == "Windows":
            print("  python setup.py")
        else:
            print("  python setup.py")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("🚀 Starting Django Development Server")
    print("="*60)
    print("\n✅ Server starting on http://localhost:8000")
    print("📝 Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    # Run Django development server
    subprocess.run([str(python_exe), "manage.py", "runserver"])

if __name__ == "__main__":
    main()
