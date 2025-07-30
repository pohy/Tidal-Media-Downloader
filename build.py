import os
import shutil
import subprocess
import glob
from pathlib import Path

def remove_if_exists(path):
    """Remove file or directory if it exists"""
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def main():
    # Clean up root directory
    remove_if_exists("dist")
    remove_if_exists("build")
    remove_if_exists("__init__.spec")

    # Find virtual environment Python executable
    venv_python = None
    possible_venv_paths = [
        os.path.join(".venv", "Scripts", "python.exe"),  # Windows
        os.path.join(".venv", "bin", "python"),          # Unix/Linux/Mac
        os.path.join("venv", "Scripts", "python.exe"),   # Alternative Windows
        os.path.join("venv", "bin", "python"),           # Alternative Unix/Linux/Mac
    ]
    
    for path in possible_venv_paths:
        if os.path.exists(path):
            venv_python = os.path.abspath(path)
            break
    
    if not venv_python:
        print("Warning: Virtual environment not found. Using system Python.")
        venv_python = "python"
    else:
        print(f"Using virtual environment Python: {venv_python}")

    # Change to TIDALDL-PY directory
    os.chdir("TIDALDL-PY")
    
    try:
        # Clean up TIDALDL-PY directory
        remove_if_exists("__init__.spec")
        remove_if_exists("dist")
        remove_if_exists("build")
        remove_if_exists("exe")
        remove_if_exists("MANIFEST.in")
        
        # Remove egg-info directories
        for egg_info in glob.glob("*.egg-info"):
            remove_if_exists(egg_info)

        # Set up environment with correct PYTHONPATH for relative imports
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.join(os.getcwd(), "tidal_dl")
        
        # Ensure required packages are installed in virtual environment
        print("Installing required build packages...")
        subprocess.run([venv_python, "-m", "pip", "install", "wheel", "pyinstaller"], check=True)
        
        # Build package
        subprocess.run([venv_python, "setup.py", "sdist", "bdist_wheel"], check=True, env=env)
        
        # Create executable with pyinstaller
        subprocess.run([venv_python, "-m", "PyInstaller", "-F", "tidal_dl/__init__.py"], check=True, env=env)
        
        # Create exe directory and move executable
        os.makedirs("exe", exist_ok=True)
        shutil.move("dist/__init__.exe", "exe/tidal-dl.exe")
        
        # Uninstall package
        subprocess.run([venv_python, "-m", "pip", "uninstall", "-y", "tidal-dl"], check=True, env=env)
        
    finally:
        # Return to parent directory
        os.chdir("..")

if __name__ == "__main__":
    main()