"""
Pizza Store - Menu Module
==========================
This module contains all menu display functions and category handlers
for the pizza store ordering system. It's separated from the main
application logic to keep the code organized and maintainable.

Author: Your Name
Date: November 2025
Version: 1.0
"""

# ============================================================================
# imports
# ============================================================================
from . import Key_press
import os
from . import cart
from . import mains
from. import drinks
from. import deserts
from . import sides

# ============================================================================
# assign imports a verisable name
# ============================================================================

enter_key_wait= Key_press.wait_for_enter
confirm_wait= Key_press.wait_for_confirm

# ============================================================================
# MENU DISPLAY FUNCTIONS
# ============================================================================
def clear_screen():
    """Clear the console screen for better readability."""
    os.system("cls" if os.name == 'nt' else 'clear')



def display_main_menu():
    """
    Display the main menu options to the user.
    
    Shows all available categories and actions including:
    - Food categories (mains, sides, desserts)
    - Beverages
    - Cart management
    - Exit option
    """
    clear_screen()
    print("\n" + "=" * 50)
    print("🍕 WELCOME TO PIZZA PARADISE 🍕")
    print("=" * 50)
    print("\nPlease select an option:")
    print("\n1. Mains (Pizzas)")
    print("2. Sides")
    print("3. Drinks")
    print("4. Dessert")
    print("5. View Cart")
    print("6. Exit")
    print("\n" + "-" * 50)


# ============================================================================
# MENU CATEGORY FUNCTIONS
# ============================================================================

def show_mains():
    """
    Display the mains menu (pizzas).
    
    This function would show available pizza options with prices.
    Currently displays a placeholder message.
    
    TODO: Add actual pizza menu items with prices
    TODO: Implement add-to-cart functionality
    """
    clear_screen()
    mains.mains_show_mains()
    ## Press Enter to return to main menu...
    # enter_key_wait()


def show_sides():
    """
    Display the sides menu.
    
    This function would show available side dishes with prices.
    Currently displays a placeholder message.
    
    TODO: Add actual side menu items with prices
    TODO: Implement add-to-cart functionality
    """
    clear_screen()
    # print("\n" + "=" * 50)
    # print("🍟 SIDES")
    # print("=" * 50)
    # print("\n[This section will display side options]")
    # ## Press Enter to return to main menu...
    sides.sides_show_sides()
    # enter_key_wait()


def show_drinks():
    """
    Display the drinks menu.
    
    This function would show available beverage options with prices.
    Currently displays a placeholder message.
    
    TODO: Add actual drink menu items with prices
    TODO: Implement add-to-cart functionality
    """
    clear_screen()
    # print("\n" + "=" * 50)
    # print("🥤 DRINKS")
    # print("=" * 50)
    # print("\n[This section will display drink options]")
    drinks.drinks_show_drinks()
    ## Press Enter to return to main menu...
    # enter_key_wait()


def show_dessert():
    """
    Display the dessert menu.
    
    This function would show available dessert options with prices.
    Currently displays a placeholder message.
    
    TODO: Add actual dessert menu items with prices
    TODO: Implement add-to-cart functionality
    """
    clear_screen()  
    # print("\n" + "=" * 50)
    # print("🍰 DESSERT")
    # print("=" * 50)
    # print("\n[This section will display dessert options]")
    deserts.deserts_show_deserts()
    ## Press Enter to return to main menu...    
    # enter_key_wait()


def show_cart():
    """
    Display the shopping cart contents.
    
    This function would show all items added to cart with quantities,
    prices, and total amount. Currently displays a placeholder message.
    
    TODO: Implement cart storage (list or dictionary)
    TODO: Display cart items with quantities and prices
    TODO: Calculate and show total price
    TODO: Add checkout functionality
    """
    clear_screen()  
    cart.show_cart_menu()
    ## Press Enter to return to main menu...
    #enter_key_wait()


# ============================================================================
# USER INPUT HANDLING
# ============================================================================

def get_user_choice():
    """
    Get and validate user input for menu selection.
    
    Returns:
        str: The user's menu choice as a string
    
    Note:
        Input is returned as string to allow for flexible validation
        and future expansion (e.g., accepting 'q' for quit)
    """
    choice = input("\nEnter your choice (1-6): ").strip()
    return choice


def show_invalid_choice():
    """
    Display an error message for invalid menu choices.
    
    This provides a consistent error message across the application
    when users enter invalid options.
    """
    clear_screen()
    print("\n❌ Invalid choice! Please enter a number between 1 and 6.")
    # Press Enter to continue...

    enter_key_wait()


def show_exit_message():
    """
    Display a farewell message when the user exits the application.
    
    This provides a friendly goodbye message to enhance user experience.
    """
    clear_screen()
    print("\n" + "=" * 50)
    print("Thank you for visiting Pizza Paradise!")
    print("Have a great day! 🍕")
    print("=" * 50 + "\n")
    enter_key_wait()
    clear_screen()
# ============================================================================