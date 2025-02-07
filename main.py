# imports
import os
import platform
import time
import requests
from beaupy import confirm, prompt, select
from beaupy.spinners import *
from rich import print
from rich.console import Console
from pyfiglet import Figlet

# Constants
SERVER_MESSAGE_URL = 'https://raw.githubusercontent.com/skiddude/Zyphral/refs/heads/main/server_message.txt'
logo = """
▒███████▒▓██   ██▓ ██▓███   ██░ ██  ██▀███   ▄▄▄       ██▓    
▒ ▒ ▒ ▄▀░ ▒██  ██▒▓██░  ██▒▓██░ ██▒▓██ ▒ ██▒▒████▄    ▓██▒    
░ ▒ ▄▀▒░   ▒██ ██░▓██░ ██▓▒▒██▀▀██░▓██ ░▄█ ▒▒██  ▀█▄  ▒██░    
  ▄▀▒   ░  ░ ▐██▓░▒██▄█▓▒ ▒░▓█ ░██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░    
▒███████▒  ░ ██▒▓░▒██▒ ░  ░░▓█▒░██▓░██▓ ▒██▒ ▓█   ▓██▒░██████▒
░▒▒ ▓░▒░▒   ██▒▒▒ ▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░
░░▒ ▒ ░ ▒ ▓██ ░▒░ ░▒ ░      ▒ ░▒░ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░
░ ░ ░ ░ ░ ▒ ▒ ░░  ░░        ░  ░░ ░  ░░   ░   ░   ▒     ░ ░   
  ░ ░     ░ ░               ░  ░  ░   ░           ░  ░    ░  ░
░         ░ ░                                                 
"""
MENU_OPTIONS = [
    "FastFlags Editor",
    "Client Settings",
    "Tweaks and Patches",
    "Settings",
    "About",
    "Quit",
]
CLIENT_SETTINGS = [
    "Disable Telemetry",
    "Mouse Cursor",
    "FPS Cap",
    "Preferred emoji type",
    "Go Back",
]
TWEAKS_PATCHES = [
    "Bring Back the Old 'Off' Sound",
    "Custom Client Font",
    "Custom Sun Texture",
    "Custom Moon Texture",
]

# Initialize consoles
console = Console()
error_console = Console(style="white on red")
sub_text = Console(style="dim white")

# Initialize spinners
spinner1 = Spinner(DOTS, "Loading Stuff...")
update_spinner = Spinner(DOTS, "Checking for updates...")
ratting_spinner = Spinner(DOTS, "Taking your personal info...")

# Functions
def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if platform.system() == "Windows" else 'clear')

def fetch_server_message():
    """Fetch the server message from the given URL."""
    try:
        response = requests.get(SERVER_MESSAGE_URL, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        error_console.print(f"Failed to fetch server message: {e}")
        return None

def display_server_message():
    """Display the server message."""
    server_message = fetch_server_message()
    if server_message:
        console.print("Server Message:", style="bold")
        console.print(server_message)
    else:
        error_console.print("Failed to retrieve server message.")

def display_logo():
    """Display the Zyphral logo."""
    console.print(logo, justify="center")

def run_spinner(spinner, duration=2):
    """Run a spinner for a specified duration."""
    spinner.start()
    time.sleep(duration)
    spinner.stop()

def main_menu():
    """Display the main menu and return the selected option."""
    console.print("Please choose an option:", style="bold")
    return select(MENU_OPTIONS, cursor=">", cursor_style="white")

def fastflag_menu():
    """Handle the FastFlags Editor menu."""
    clear_console()
    console.print("WARNING", style="bold white on red", justify="center")
    console.print("Please use this with caution", justify="center")
    console.print("Misusing this can lead to instability or unexpected behavior.", justify="center")
    time.sleep(5)
    clear_console()
    display_logo()
    display_server_message()
    console.print("FastFlags Editor:", style="bold")
    # Placeholder for FastFlags Editor functionality

def clientsettings_menu():
    """Handle the Client Settings menu."""
    clear_console()
    display_logo()
    display_server_message()
    client_setting = select(CLIENT_SETTINGS, cursor=">", cursor_style="white")

    if client_setting == "Disable Telemetry":
        clear_console()
        display_logo()
        display_server_message()
        if confirm("Disable Telemetry?"):
            console.print("Telemetry disabled.", style="bold green")

    elif client_setting == "FPS Cap":
        clear_console()
        display_logo()
        display_server_message()
        fps_cap = prompt("Enter FPS Cap:")
        console.print(f"FPS Cap set to {fps_cap}.", style="bold green")

    elif client_setting == "Go Back":
        main_menu()

def tweaksandpatches_menu():
    """Handle the Tweaks and Patches menu."""
    clear_console()
    display_logo()
    display_server_message()
    tweak_patch = select(TWEAKS_PATCHES, cursor=">", cursor_style="white")
    if tweak_patch == "Bring Back the Old 'Off' Sound":
        if confirm("Bring Back the Old 'Off' Sound?"):
            console.print("Old 'Off' sound restored.", style="bold green")

def settings_menu():
    """Handle the Settings menu."""
    clear_console()
    display_logo()
    display_server_message()
    console.print("Settings menu:", style="bold")
    # Placeholder for settings functionality

def about_menu():
    """Display information about Zyphral."""
    console.print("""
Zyphral is a Roblox bootstrapper made in Python and doesn't work at all.
It is made by one person, and that's me!
GitHub repo: https://github.com/skiddude/Zyphral/
Website: https://skiddude.github.io/zyphral
""")

def quit_menu():
    """Handle the Quit menu option."""
    clear_console()
    console.print("Quitting Zyphral...", style="bold red")
    time.sleep(1)
    clear_console()

def run_menu():
    """Run the main menu loop."""
    while True:
        menu_option = main_menu()

        if menu_option == "FastFlags Editor":
            fastflag_menu()
        elif menu_option == "Client Settings":
            clientsettings_menu()
        elif menu_option == "Tweaks and Patches":
            tweaksandpatches_menu()
        elif menu_option == "Settings":
            settings_menu()
        elif menu_option == "About":
            about_menu()
        elif menu_option == "Quit":
            quit_menu()
            break  # Exit the program

# Main execution
if __name__ == "__main__":
    clear_console()
    run_spinner(spinner1)
    run_spinner(ratting_spinner)
    run_spinner(update_spinner)
    display_logo()
    display_server_message()
    run_menu()