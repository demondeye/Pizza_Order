"""
Mains Menu Module
=================
Contains the drink menu items and display logic for the mains category.
Allows customers to browse drinks and add them to their cart.

Author: Your Name
Date: November 2025
Version: 1.0
"""

# ============================================================================
# IMPORTS
# ============================================================================
from . import cart
from .Key_press import wait_for_enter, wait_for_confirm, clear_screens

# Create the variable for enter key waiting
enter_key_wait = wait_for_enter
clear_screen = clear_screens
confirm_wait = wait_for_confirm

# ============================================================================
# drink MENU DATA
# ============================================================================

# Dictionary of available drinks with their prices
drinks = {
    '1': {'name': 'Cola', 'price': 4.50},
    '2': {'name': 'Fanta', 'price': 4.50},
    '3': {'name': 'leononaid', 'price': 4.50,},
    '4': {'name': 'Lemon Lime and bitters', 'price': 5.50,},
    '5': {'name': 'Diet cola', 'price': 44.50,},
    '6': {'name': 'Pepsie', 'price': 4.50,},
    '7': {'name': 'DR pepper', 'price': 5.99,},
   
}


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_drink_menu():
    """
    Display all available drinks with prices and descriptions.
    
    Shows a formatted list of all drink options that customers
    can choose from and add to their cart.
    """
    print("\n" + "=" * 70)
    print("🍕 MAINS - drinks")
    print("=" * 70)
    print()
    
    for key, drink in drinks.items():
        print(f"{key}. {drink['name']:<25} ${drink['price']:>6.2f}")
        # print(f"   {drink['description']}")
        print()
    
    print("9. Back to main menu")
    print("-" * 70)


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def drinks_show_drinks():
    """
    Main function to display mains menu and handle user selection.
    
    This is the main entry point called from the menu system.
    Displays the drink menu and allows users to add items to cart.
    """
    while True:
        # Display the drink menu
        clear_screen()
        display_drink_menu()
        
        # Get user's choice
        choice = input("\nEnter your choice (1-9): ").strip()
        
        # Check if user wants to go back
        if choice == '9':
            return
        
        # Check if choice is valid
        if choice in drinks:
            drink = drinks[choice]
            
            # Ask for quantity with validation
            while True:
                clear_screen()
                display_drink_menu()
                print(f"\nSelected: {drink['name']} - ${drink['price']:.2f}")
                clear_screen()
                quantity_input = input(f"\nHow many would you like? (1-20, Enter for 1): ").strip()
                
                # If empty, default to 1
                if quantity_input == '':
                    quantity = 1
                    break
                
                try:
                    quantity = int(quantity_input)
                    
                    # Validate quantity
                    if quantity <= 0:
                        clear_screen()
                        print("\n❌ Quantity must be greater than 0!")
                        enter_key_wait()
                        continue
                    elif quantity > 20:
                        clear_screen()
                        print(f"\n❌ Maximum quantity is 20 per item! You entered: {quantity}")
                        enter_key_wait()
                        continue
                    else:
                        # Valid quantity
                        break
                        
                except ValueError:
                    clear_screen()
                    print("\n❌ Invalid quantity! Please enter a number.")
                    enter_key_wait()
                    continue
            
            # Add to cart
            cart.add_item(drink['name'], drink['price'], quantity)
            print(f"\n💰 Subtotal: ${drink['price'] * quantity:.2f}")
            # clear_screen()
            enter_key_wait()
            
        else:
            # Invalid choice
            clear_screen()
            print("\n❌ Invalid choice! Please select a number from 1-9.")
            enter_key_wait()


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_drink_by_name(drink_name):
    """
    Get drink details by name.
    
    Args:
        drink_name (str): Name of the drink
    
    Returns:
        dict: drink details or None if not found
    """
    for drink in drinks.values():
        if drink['name'].lower() == drink_name.lower():
            return drink
    return None


def get_all_drinks():
    """
    Get all available drinks.
    
    Returns:
        dict: Dictionary of all drinks
    """
    return drinks.copy()