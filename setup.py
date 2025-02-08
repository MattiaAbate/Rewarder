import platform
import subprocess

print("Welcome to the setup script for RewarderBot!")

install_packages = input("Do you want to install the required packages? (Y/N): ")

while True:
    match install_packages.lower():
        case "y" | "yes":
            print("Installing the required packages...")
            if platform.system() == "Windows":
                result = subprocess.run(['cmd.exe', '/c', 'pip install -r requirements.txt'], shell=True)
            elif platform.system() == "Darwin":
                result = subprocess.run(['python3', '-m', 'pip', 'install', '-r', 'requirements.txt'])
            elif platform.system() == "Linux":
                result = subprocess.run(['python3', '-m', 'pip', 'install', '-r', 'requirements.txt'])
            else:
                result = None
                print(f"Your operative system ({platform.system}) isn't supported. OS supported: Windows, MacOS and Linux.")
            
            if result and result.returncode == 0:
                print(f"Required packages installed correctly!")
            else:
                print(f"An error occured during libraries installation!\nError:\n\t{result.stderr}")
    
            break
        case "n" | "no":
            print("Required packages installation skipped.\nWithout packages, the application may not work properly.")
            break
        case "h" | "help" | "?":
            print("""
            Help panel:
                Libraries:
                - discord for discord.py library
                - dotenv for dotenv library
                - requests for requests library
                - asyncio for asyncio library
            """)
        case _:
            print("Invalid input. Please enter 'Y' or 'N'.")

print("Setup completed! You can now close this window.")

start_app = input("Do you want to start the application? (Y/N): ")

while True:
    match start_app.lower():
        case "y":
            print("Starting the application...")
            subprocess.run(["python", "main.py"])
            exit()
            break
        case "n":
            exit()
            break
        case _:
            print("Invalid input. Please enter 'Y' or 'Y'.")