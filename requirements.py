import subprocess
import sys
import os

def install_requirements():
    requirements = [
        'PyQt6>=6.4.0',
        'openai>=1.0.0',
        'keyboard>=0.13.5',
        'requests>=2.28.0',
        'python-dotenv>=0.19.0',
        'colorama>=0.4.4',  # For colored terminal output
        'tqdm>=4.65.0'      # For progress bars
    ]
    
    print("\n=== GVTech-HUB_ChatGPT Requirements Installer ===")
    print("Installing required packages...\n")
    
    success = True
    for package in requirements:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error installing {package}: {e}")
            success = False
    
    if success:
        print("\n✓ All requirements installed successfully!")
        print("\nYou can now run GVTech-HUB_ChatGPT using:")
        print("python src/main.py")
    else:
        print("\n✗ Some packages failed to install. Please check the errors above.")
    
    return success

if __name__ == "__main__":
    try:
        install_requirements()
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {e}")
        sys.exit(1)