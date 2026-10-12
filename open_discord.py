import os
import getpass

# Get your current Windows username dynamically
username = getpass.getuser()

# The standard installation path for Discord on Windows
discord_path = f"C:\\Users\\{username}\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"

try:
    os.system(discord_path)
    print("Opening Discord...")
except Exception as e:
    print(f"Could not open Discord. Error: {e}")
