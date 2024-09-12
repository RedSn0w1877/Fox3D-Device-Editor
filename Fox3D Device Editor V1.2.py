import time
import os
import random

def ask_confirmation(text):
    while True:
        confirm = input(f"{text} (yes/no): ").lower()
        if confirm in ["yes", "no"]:
            return confirm == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def print_progress_bar(progress, total):
    bar_length = 75
    filled_length = int(progress / total * bar_length)
    bar = "[" + "=" * filled_length + " " * (bar_length - filled_length) + "]"

    if progress >= 50:
        print(f"\rProgress: {bar} Installing... {progress}/{total}", end="")
    else:
        print(f"\rProgress: {bar} {progress}/{total}", end="")

def main_menu():
    print("-Fox3D Chromebook modifier-")
    print("Options:")
    print("1. Unblock extensions")
    print("2. Jailbreak")
    print("3. Developer mode")

    choice = input("Please type a number: ")
    return choice

while True:
    choice = main_menu()

    if choice == "1":
        confirm_response = ask_confirmation(
            "Are you sure you want to do this? This action could result in fatal consequences."
        )

        if confirm_response:
            
            print("Confirmed! Continuing...")
            print("Please note! I am not responsible for bricked devices, dead SD cards, or you getting sued because your alarm clock didn't wake you up.")
            print("If you did something stupid and point the finger at me, I will laugh at you. Wait 5 seconds.")
            time.sleep(5)
            print("Final warning. Do you want to do this?")
            confirm = input()

            if confirm == "no":
                print("Redirecting to menu...")
            elif confirm == "yes":
                print("Downloading files and patching flags...")
                for i in range(101):
                    print_progress_bar(i, 100)
                    if i == 37:
                        print("\nExtracting files...")
                    elif i == 70:
                        print("\nInstalling components and Fox3D Registries...")
                    time.sleep(random.randint(200, 500) / 1000)  
                print("\nProcess completed!")
                break
        else:  
            print("Confirmation failed. Please try again.")
    else:
        print("Sorry! Still under construction.")