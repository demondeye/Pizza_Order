"""
Mains Menu Module
=================
Contains the pizza menu items and display logic for the mains category.
Allows customers to browse pizzas and add them to their cart.

Author: Your Name
Date: November 2025
Version: 1.0
"""

# ============================================================================
# IMPORTS
# ============================================================================
from . import cart
from .Key_press import wait_for_enter, wait_for_confirm, clear_screens
import time

# Create the variable for enter key waiting
enter_key_wait = wait_for_enter
clear_screen = clear_screens
confirm_wait = wait_for_confirm
wait_time=3

# ============================================================================
# PIZZA MENU DATA
# ============================================================================

# Dictionary of available pizzas with their prices
PIZZAS = {
    '1': {'name': 'Margherita Pizza', 'price': 12.99, 'description': 'Classic tomato, mozzarella, and basil'},
    '2': {'name': 'Pepperoni Pizza', 'price': 14.99, 'description': 'Loaded with pepperoni and cheese'},
    '3': {'name': 'Supreme Pizza', 'price': 16.99, 'description': 'The works - pepperoni, sausage, peppers, onions, mushrooms'},
    '4': {'name': 'Hawaiian Pizza', 'price': 15.49, 'description': 'Ham and pineapple on a cheese base'},
    '5': {'name': 'Vegetarian Pizza', 'price': 13.99, 'description': 'Loaded with fresh vegetables'},
    '6': {'name': 'BBQ Chicken Pizza', 'price': 15.99, 'description': 'Grilled chicken with BBQ sauce'},
    '7': {'name': 'Meat Lovers Pizza', 'price': 17.99, 'description': 'Pepperoni, sausage, ham, and bacon'},
    '8': {'name': 'Four Cheese Pizza', 'price': 14.49, 'description': 'Mozzarella, parmesan, cheddar, and blue cheese'}
}


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_pizza_menu():
    """
    Display all available pizzas with prices and descriptions.
    
    Shows a formatted list of all pizza options that customers
    can choose from and add to their cart.
    """
    print("\n" + "=" * 70)
    print("🍕 MAINS - PIZZAS")
    print("=" * 70)
    print()
    
    for key, pizza in PIZZAS.items():
        print(f"{key}. {pizza['name']:<25} ${pizza['price']:>6.2f}")
        print(f"   {pizza['description']}")
        print()
    
    print("9. Back to main menu")
    print("-" * 70)


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def mains_show_mains():
    """
    Main function to display mains menu and handle user selection.
    
    This is the main entry point called from the menu system.
    Displays the pizza menu and allows users to add items to cart.
    """
    while True:
        # Display the pizza menu
        clear_screen()
        display_pizza_menu()
        
        # Get user's choice
        choice = input("\nEnter your choice (1-9): ").strip()
        
        # Check if user wants to go back
        if choice == '9':
            return
        
        # Check if choice is valid
        if choice in PIZZAS:
            pizza = PIZZAS[choice]
            
            # Ask for quantity with validation
            while True:
                clear_screen()
                display_pizza_menu()
                print(f"\nSelected: {pizza['name']} - ${pizza['price']:.2f}")
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

                        #enter_key_wait()
                         #time to wait before continuing the applicaiton
                        time.sleep(wait_time)
                        continue
                    elif quantity > 20:
                        clear_screen()
                        print(f"\n❌ Maximum quantity is 20 per item! You entered: {quantity}")
                         #time to wait before continuing the applicaiton
                        time.sleep(wait_time)
                        #enter_key_wait()
                        continue
                    else:
                        # Valid quantity
                        break
                        
                except ValueError:
                    clear_screen()
                    print("\n❌ Invalid quantity! Please enter a number.")
                    # enter_key_wait()
                    #time to wait before continuing the applicaiton
                    time.sleep(wait_time)
                    continue
            
            # Add to cart
            clear_screen()
            cart.add_item(pizza['name'], pizza['price'], quantity)
            print(f"\n💰 Subtotal: ${pizza['price'] * quantity:.2f}")
            # waits for 5 seconds before continuing application
            time.sleep(wait_time)
            clear_screen()
            # enter_key_wait()
            
        else:
            # Invalid choice
            clear_screen()
            print("\n❌ Invalid choice! Please select a number from 1-9.")
            # enter_key_wait()
            #time to wait before continuing the applicaiton
            time.sleep(wait_time)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_pizza_by_name(pizza_name):
    """
    Get pizza details by name.
    
    Args:
        pizza_name (str): Name of the pizza
    
    Returns:
        dict: Pizza details or None if not found
    """
    for pizza in PIZZAS.values():
        if pizza['name'].lower() == pizza_name.lower():
            return pizza
    return None


def get_all_pizzas():
    """
    Get all available pizzas.
    
    Returns:
        dict: Dictionary of all pizzas
    """
    return PIZZAS.copy()