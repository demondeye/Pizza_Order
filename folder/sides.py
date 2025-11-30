"""
Mains Menu Module
=================
Contains the sides menu items and display logic for the mains category.
Allows customers to browse sides and add them to their cart.

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
# sides MENU DATA
# ============================================================================

# Dictionary of available sides with their prices
sides = {
    '1': {'name': 'Chips', 'price': 4.99},
    '2': {'name': 'Garlic bread', 'price': 14.99},
    '3': {'name': 'Onion rings', 'price': 16.99,},
    '4': {'name': 'Caesar salad', 'price': 15.49,},
    '5': {'name': 'Bread sticks', 'price': 13.99,},
    '5': {'name': 'Arancini balls', 'price': 13.99,},

   
}


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_sides_menu():
    """
    Display all available sides with prices and descriptions.
    
    Shows a formatted list of all sides options that customers
    can choose from and add to their cart.
    """
    print("\n" + "=" * 70)
    print("🍕 MAINS - sides")
    print("=" * 70)
    print()
    
    for key, side in sides.items():
        print(f"{key}. {side['name']:<25} ${side['price']:>6.2f}")
        # print(f"   {sides['description']}")
        print()
    
    print("9. Back to main menu")
    print("-" * 70)


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def sides_show_sides():
    """
    Main function to display mains menu and handle user selection.
    
    This is the main entry point called from the menu system.
    Displays the sides menu and allows users to add items to cart.
    """
    while True:
        # Display the sides menu
        clear_screen()
        display_sides_menu()
        
        # Get user's choice
        choice = input("\nEnter your choice (1-9): ").strip()
        
        # Check if user wants to go back
        if choice == '9':
            return
        
        # Check if choice is valid
        if choice in sides:
            side = sides[choice]
            
            # Ask for quantity with validation
            while True:
                clear_screen()
                display_sides_menu()
                print(f"\nSelected: {side['name']} - ${side['price']:.2f}")
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
            cart.add_item(side['name'], side['price'], quantity)
            print(f"\n💰 Subtotal: ${side['price'] * quantity:.2f}")
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

def get_sides_by_name(side_name):
    """
    Get sides details by name.
    
    Args:
        sides_name (str): Name of the sides
    
    Returns:
        dict: sides details or None if not found
    """
    for side in sides.values():
        if side['name'].lower() == side_name.lower():
            return side
    return None


def get_all_sides():
    """
    Get all available sides.
    
    Returns:
        dict: Dictionary of all sides
    """
    return sides.copy()