#!/usr/bin/env python
"""
Setup script for Django project - handles venv creation and dependency installation
Works on Windows, macOS, and Linux
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and report status"""
    print(f"\n{'='*60}")
    print(f"📦 {description}...")
    print(f"{'='*60}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Failed to {description}")
        sys.exit(1)
    print(f"✅ {description} complete")

def main():
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    venv_dir = project_dir / "venv"
    requirements_file = project_dir / "requirements.txt"
    
    print(f"\n🚀 Setting up Django project in: {project_dir}")
    print(f"Platform: {platform.system()}")
    
    # Create virtual environment
    if not venv_dir.exists():
        run_command(f"{sys.executable} -m venv venv", "Create virtual environment")
    else:
        print("\n✅ Virtual environment already exists")
    
    # Determine pip executable path
    if platform.system() == "Windows":
        pip_exe = venv_dir / "Scripts" / "pip.exe"
        python_exe = venv_dir / "Scripts" / "python.exe"
    else:
        pip_exe = venv_dir / "bin" / "pip"
        python_exe = venv_dir / "bin" / "python"
    
    # Upgrade pip
    run_command(f"{pip_exe} install --upgrade pip", "Upgrade pip")
    
    # Install dependencies
    if requirements_file.exists():
        run_command(f"{pip_exe} install -r requirements.txt", "Install dependencies")
    else:
        print(f"⚠️  requirements.txt not found in {project_dir}")
        sys.exit(1)
    
    # Run migrations
    run_command(f"{python_exe} manage.py migrate", "Run database migrations")
    
    print("\n" + "="*60)
    print("✅ Setup complete!")
    print("="*60)
    print("\nTo start the development server, run:")
    if platform.system() == "Windows":
        print("  • run.bat (Windows)")
        print("  OR")
        print("  • python run_server.py")
    else:
        print("  • ./run.sh (macOS/Linux)")
        print("  OR")
        print("  • python run_server.py")
    print("\nThen visit: http://localhost:8000")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
