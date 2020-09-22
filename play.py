"""
Primary file for PLAY section of game

Consider npyscreen (https://npyscreen.readthedocs.io/index.html) to utilize for UI

"""

from setup import *


def display_menu(menu: int):
    print(MENUS[menu])
    action = get_user_input("user@pc>")
    if action == "login":
        display_menu(2)
    elif action == "settings":
        display_menu(1)
    else:
        print("Invalid action...")
        get_user_input("user@pc>")


def get_user_input(prompt: str):
    return input(prompt).strip().lower()
