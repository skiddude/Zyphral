# imports
import os
import platform
import sys
import requests
import time
from beaupy import confirm, prompt, select, select_multiple
from beaupy.spinners import *
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from pyfiglet import Figlet
# end of imports

# vars
console = Console()
error_console = Console(style="white on red")
sub_text = Console(style="dim white")
spinner1 = Spinner(DOTS, "Loading Stuff...")
update_spinner = Spinner(DOTS, "Checking for updates...")
ratting_spinner = Spinner(DOTS, "Taking your personal info...")
server_message_url = 'https://raw.githubusercontent.com/skiddude/Zyphral/refs/heads/main/server_message.txt'
server_message_response = requests.get(server_message_url)

# defs
def clear_console():
    # Check the operating system
    if platform.system() == "Windows":
        os.system('cls')  # Clear for Windows
    else:
        os.system('clear')


def server_message():
    print("Server Message:")
    if server_message_response.status_code == 200:
        servermessage = server_message_response.text
        print(servermessage)  # Make sure to print the server message
    else:
        error_console.print("Failed to get server message:")
        sub_text.print(server_message_response.status_code)


clear_console()

# spinners
spinner1.start()
time.sleep(2)
spinner1.stop()
ratting_spinner.start()
time.sleep(2)
ratting_spinner.stop()
update_spinner.start()
time.sleep(2)
update_spinner.stop()

logo_font = Figlet(font="bloody")
logo = logo_font.renderText('Zyphral')

#menu options
menu_options = [
    "FastFlags Editor",
    "Client Settings",
    "Tweaks and Patches",
    "Settings",
    "Quit",
]

client_settings = [
    "Disable Telemetry",
    "Disable FPS cap",
    "FPS Cap",
    "Launcher",
    "Polling Delay",
    "Automatic APK Updates",
    "Disable APK Verification",
    "Go Back",
]

tweaks_patches = [
    "Bring Back the Old 'Off' Sound",
    "Custom Client Font",
    "Custom Sun Texture",
    "Custom Moon Texture",
]

clear_console()
console.print(logo)
server_message()

def main_menu():
    console.print("Please choose an option:")
    return select(menu_options, cursor=">", cursor_style="white")

def fastflag_menu():
    clear_console()
    console.print(logo, justify="center")
    server_message()
    console.print("FastFlags Editor menu:")
    # Example of handling a specific option in the FastFlags menu

def clientsettings_menu():
    clear_console()
    print(logo)
    server_message()
    client_setting = select(client_settings, cursor=">", cursor_style="white")
    if client_setting == "Go Back":
        main_menu()

def tweaksandpatches_menu():
    clear_console()
    print(logo)
    server_message()
    tweak_patch = select(tweaks_patches, cursor=">", cursor_style="white")
    print("1. Example Option 1")

def settings_menu():
    clear_console()
    print(logo)
    server_message()
    print("Settings menu:")
    # Placeholder for settings options

def quit_menu():
    clear_console()
    print("Quitting Zyphral...")

# Main logic to navigate between menus
def run_menu():
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
        elif menu_option == "Quit":
            quit_menu()
            break  # Exit the program

run_menu()