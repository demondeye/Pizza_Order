"""
Pizza Store - Main Application
===============================
This is the main entry point for the pizza store ordering system.
It imports the menu module and handles the main application loop.

Author: mattehw
Date: November 2025
Version: 1.0

Usage:
    python main.py
"""

# ============================================================================
# IMPORTS
# ============================================================================
import sys
import os
# Import all menu functions from the menu module
from folder import (
    display_main_menu,
    get_user_choice,
    show_mains,
    show_sides,
    show_drinks,
    show_dessert,
    show_cart,
    show_invalid_choice,
    show_exit_message
)
from folder import Key_press

enter_key_wait= Key_press.wait_for_enter
confirm_wait= Key_press.wait_for_confirm
clear_screen= Key_press.clear_screens

# ============================================================================
# MAIN APPLICATION LOGIC
# ============================================================================

def process_menu_choice(choice):
    """
    Process the user's menu selection and call appropriate function.
    
    Args:
        choice (str): The user's menu selection (1-6)
    
    Returns:
        bool: True if program should continue, False if user wants to exit
    
    This function acts as a router, directing the user's choice to the
    appropriate menu function from the menu module.
    """
    if choice == '1':
        show_mains()
        return True
    elif choice == '2':
        show_sides()
        return True
    elif choice == '3':
        show_drinks()
        return True
    elif choice == '4':
        show_dessert()
        return True
    elif choice == '5':
        show_cart()
        return True
    elif choice == '6':
        # User wants to exit
        clear_screen()
        print("\n" + "=" * 60)
        print("You are about to Exit the Pizza Ordering System.")
        print("=" * 60)
        user_choice = confirm_wait("Are you sure you want to exit? (y/n): ")
        if user_choice == 'y':
            show_exit_message()
            return False
        else: return True
    else:
        # Invalid choice
        show_invalid_choice()
        return True


def main():
    """
    Main application loop.
    
    Continuously displays the main menu and processes user selections
    until the user chooses to exit. This is the core of the application
    that ties everything together.
    
    Flow:
        1. Display main menu (from menu module)
        2. Get user choice (from menu module)
        3. Process choice (local function)
        4. Repeat until exit
    """
    # Main program loop - runs until user exits
    while True:
        # Display the main menu
        display_main_menu()
        
        # Get user's choice
        choice = get_user_choice()
        
        # Process the choice and check if we should continue
        should_continue = process_menu_choice(choice)
        
        # Exit loop if user chose to quit
        if not should_continue:
            break


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    Entry point for the application.
    
    This block ensures the main() function only runs when the script
    is executed directly, not when imported as a module.
    
    It also handles keyboard interrupts (Ctrl+C) gracefully to provide
    a better user experience.
    """
    try:
        # Start the application
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\n" + "=" * 50)
        print("Program interrupted by user.")
        print("Thank you for visiting Pizza Paradise!")
        print("=" * 50 + "\n")
        # enter_key_wait()
        sys.exit(0)