"""
Mains Menu Module
=================
Contains the deserts menu items and display logic for the mains category.
Allows customers to browse deserts and add them to their cart.
main desert code was done by Joy Kisby but edited by matthew redman to fit program structure within the cart 

Author: Joy Kisby
edited by matthew 
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
# deserts MENU DATA
# ============================================================================

# Dictionary of available deserts with their prices
# Joys  code but layed out to be accepted my the program layout
deserts = {
    '1': {'name': 'Tiramisu', 'price': 8.50},
    '2': {'name': 'Chocolate Mousse', 'price': 7.99},
    '3': {'name': 'Cannoli', 'price': 10.99,},
    '4': {'name': 'Sticky Date Pudding', 'price': 12.50,},
    '5': {'name': 'Cheesecake', 'price': 11.99,},

   
}


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_deserts_menu():
    """
    Display all available deserts with prices and descriptions.
    
    Shows a formatted list of all deserts options that customers
    can choose from and add to their cart.
    """
    print("\n" + "=" * 70)
    print("🍕 MAINS - deserts")
    print("=" * 70)
    print()
    
    for key, desert in deserts.items():
        print(f"{key}. {desert['name']:<25} ${desert['price']:>6.2f}")
        # print(f"   {deserts['description']}")
        print()
    
    print("9. Back to main menu")
    print("-" * 70)


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def deserts_show_deserts():
    """
    Main function to display mains menu and handle user selection.
    
    This is the main entry point called from the menu system.
    Displays the deserts menu and allows users to add items to cart.
    """
    while True:
        # Display the deserts menu
        clear_screen()
        display_deserts_menu()
        
        # Get user's choice
        choice = input("\nEnter your choice (1-9): ").strip()
        
        # Check if user wants to go back
        if choice == '9':
            return
        
        # Check if choice is valid
        if choice in deserts:
            desert = deserts[choice]
            
            # Ask for quantity with validation
            while True:
                clear_screen()
                display_deserts_menu()
                print(f"\nSelected: {desert['name']} - ${desert['price']:.2f}")
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
            cart.add_item(desert['name'], desert['price'], quantity)
            print(f"\n💰 Subtotal: ${desert['price'] * quantity:.2f}")
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

def get_deserts_by_name(desert_name):
    """
    Get deserts details by name.
    
    Args:
        deserts_name (str): Name of the deserts
    
    Returns:
        dict: deserts details or None if not found
    """
    for desert in deserts.values():
        if desert['name'].lower() == desert_name.lower():
            return desert
    return None


def get_all_deserts():
    """
    Get all available deserts.
    
    Returns:
        dict: Dictionary of all deserts
    """
    return deserts.copy()