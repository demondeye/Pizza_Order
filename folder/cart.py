"""
Shopping Cart Module
====================
Manages the shopping cart for the pizza store.
Tracks items, quantities, and calculates totals.

Author: Your Name
Date: November 2025
Version: 1.0
"""

# ============================================================================
# IMPORTS
# ============================================================================
from .Key_press import wait_for_enter, wait_for_confirm, clear_screens
import datetime

# Create the variable for enter key waiting
enter_key_wait = wait_for_enter
confirm_wait = wait_for_confirm
clear_screen = clear_screens


# ============================================================================
# CART DATA STRUCTURE
# ============================================================================

# Global cart dictionary to store items
# Structure: {item_name: {'price': float, 'quantity': int}}
_cart = {}


# ============================================================================
# CART FUNCTIONS
# ============================================================================

def add_item(item_name, price, quantity=1):
    """
    Add an item to the cart or update quantity if it already exists.
    
    Args:
        item_name (str): Name of the item
        price (float): Price per unit
        quantity (int): Number of items to add (default: 1)
    
    Returns:
        bool: True if successful
    """
    if item_name in _cart:
        # Item already exists, increase quantity
        _cart[item_name]['quantity'] += quantity
    else:
        # New item, add to cart
        _cart[item_name] = {
            'price': price,
            'quantity': quantity
        }
    print(f"✓ Added {quantity}x {item_name} to cart")
    return True


def remove_item(item_name):
    """
    Remove an item completely from the cart.
    
    Args:
        item_name (str): Name of the item to remove
    
    Returns:
        bool: True if successful, False if item not found
    """
    if item_name in _cart:
        del _cart[item_name]
        print(f"✓ Removed {item_name} from cart")
        return True
    else:
        print(f"✗ {item_name} not found in cart")
        return False


def get_cart():
    """
    Get the entire cart contents.
    
    Returns:
        dict: Copy of the cart dictionary
    """
    return _cart.copy()


def get_cart_count():
    """
    Get the total number of items in the cart.
    
    Returns:
        int: Total quantity of all items
    """
    return sum(item['quantity'] for item in _cart.values())


def get_cart_total():
    """
    Calculate the total price of all items in the cart.
    
    Returns:
        float: Total price
    """
    total = 0.0
    for item in _cart.values():
        total += item['price'] * item['quantity']
    return total


def clear_cart():
    """
    Remove all items from the cart.
    """
    global _cart
    _cart = {}
    print("✓ Cart cleared")


def is_empty():
    """
    Check if the cart is empty.
    
    Returns:
        bool: True if cart is empty, False otherwise
    """
    return len(_cart) == 0


def display_cart():
    """
    Display the cart contents in a formatted way.
    
    Returns:
        str: Formatted cart display
    """
    if is_empty():
        return "\n❌ Your cart is empty."
    
    output = "\n" + "=" * 60 + "\n"
    output += "ITEM                          PRICE    QTY    SUBTOTAL\n"
    output += "-" * 60 + "\n"
    
    for item_name, details in _cart.items():
        price = details['price']
        quantity = details['quantity']
        subtotal = price * quantity
        output += f"{item_name:<25} ${price:>6.2f}  x{quantity:<3}  ${subtotal:>7.2f}\n"
    
    output += "-" * 60 + "\n"
    output += f"{'TOTAL:':<47} ${get_cart_total():>7.2f}\n"
    output += "=" * 60 + "\n"
    
    return output


# ============================================================================
# MAIN CART VIEW FUNCTION (Use this in your menu!)
# ============================================================================

def show_cart_menu():
    """
    Main function to display and manage cart from the main menu.
    This is the function you should call from show_cart() in menu.py
    
    Displays cart and provides options to:
    - Proceed to checkout
    - Clear the cart
    - Return to main menu
    """
    
    # If cart is empty, show empty cart menu
    if is_empty():
        cart_empty_menu()
    else:
        while True:
            clear_screen()
            print("\n" + "=" * 60)
            print("🛒 YOUR SHOPPING CART")
            print("=" * 60)
            
            # Display cart contents
            print(display_cart())
            
            # Show management options for non-empty cart
            print("\nWhat would you like to do?")
            print("1. Proceed to Checkout")
            print("2. Clear Cart")
            print("3. Return to Main Menu")
                
            choice = input("\nEnter your choice (1-3): ").strip()
                
            if choice == '1':
                # Checkout process
                order = {
                    'items': get_cart(),
                    'total': get_cart_total(),
                    'item_count': get_cart_count()
                }
                
                # Ask for delivery or pickup
                confirm = confirm_wait("Do you want Delivery for the order? (y/n): ")
                
                # Get current date and time
                now = datetime.datetime.now()
                date_string_and_time = now.strftime("%d-%m-%y %I:%M %p")
                date_string = now.strftime("%d-%m-%y")
                
                # Get customer information
                name = input("Enter your name for the order: ")
                phoneNumber = input("Enter your phone number for the order: ")
                
                if confirm == 'y':
                    # Delivery order
                    address = input("Enter your address for the order: ")
                    
                    # Open file for appending
                    receit = open(f"orders_{date_string}.txt", "a")
                    
                    # Write to file
                    receit.write("\n" + "=" * 60 + "\n")
                    receit.write(f"ORDER TICKET - DELIVERY - {date_string_and_time}\n")
                    receit.write("=" * 60 + "\n")
                    receit.write(f"Customer: {name}\n")
                    receit.write(f"Phone: {phoneNumber}\n")
                    receit.write(f"Address: {address}\n")
                    receit.write("-" * 60 + "\n")
                    
                    # Write order items
                    for item_name, details in order['items'].items():
                        receit.write(f"{item_name} x{details['quantity']} - ${details['price'] * details['quantity']:.2f}\n")
                    
                    receit.write("-" * 60 + "\n")
                    receit.write(f"TOTAL: ${order['total']:.2f}\n")
                    receit.write(f"Total Items: {order['item_count']}\n")
                    receit.write("=" * 60 + "\n\n")
                    receit.close()
                    
                    # Show confirmation
                    print("\n" + "=" * 60)
                    print("✓ ORDER CONFIRMED! DELIVERY")
                    print("=" * 60)
                    print(f"\nCustomer: {name}")
                    print(f"Phone: {phoneNumber}")
                    print(f"Address: {address}")
                    print(f"\nTotal Items: {order['item_count']}")
                    print(f"Total Amount: ${order['total']:.2f}")
                    print(f"\nOrder Date: {date_string_and_time}")
                    print("\nThank you for your order!")
                    print("Your delicious food will be delivered soon! 🍕")
                    
                else:
                    # Pickup order
                    receit = open(f"orders_{date_string}.txt", "a")
                    
                    # Write to file
                    receit.write("\n" + "=" * 60 + "\n")
                    receit.write(f"ORDER TICKET - PICKUP - {date_string_and_time}\n")
                    receit.write("=" * 60 + "\n")
                    receit.write(f"Customer: {name}\n")
                    receit.write(f"Phone: {phoneNumber}\n")
                    receit.write("-" * 60 + "\n")
                    
                    # Write order items
                    for item_name, details in order['items'].items():
                        receit.write(f"{item_name} x{details['quantity']} - ${details['price'] * details['quantity']:.2f}\n")
                    
                    receit.write("-" * 60 + "\n")
                    receit.write(f"TOTAL: ${order['total']:.2f}\n")
                    receit.write(f"Total Items: {order['item_count']}\n")
                    receit.write("=" * 60 + "\n\n")
                    receit.close()
                    
                    # Show confirmation
                    print("\n" + "=" * 60)
                    print("✓ ORDER CONFIRMED! PICKUP")
                    print("=" * 60)
                    print(f"\nCustomer: {name}")
                    print(f"Phone: {phoneNumber}")
                    print(f"\nTotal Items: {order['item_count']}")
                    print(f"Total Amount: ${order['total']:.2f}")
                    print(f"\nOrder Date: {date_string_and_time}")
                    print("\nThank you for your order!")
                    print("Your delicious food will be ready soon! 🍕")
                
                # Clear cart after checkout
                clear_cart()
                enter_key_wait()
                return
                    
            elif choice == '2':
                # Clear cart with confirmation
                confirm = confirm_wait("Are you sure you want to clear the cart? (y/n): ")       
                if confirm == 'y':
                    clear_cart()
                    clear_screen()
                    print("Cart has been cleared.")
                    enter_key_wait()
                else:
                    print("Cart not cleared.")
                    enter_key_wait()
                    
            elif choice == '3':
                # Return to main menu
                return
                    
            else:
                clear_screen()
                print("\n❌ Invalid choice!")
                enter_key_wait()


def cart_empty_menu():
    """Display menu when cart is empty."""
    while True:
        # Show management options for empty cart
        clear_screen()
        print("\n" + "=" * 60)
        print("🛒 YOUR SHOPPING CART")
        print("=" * 60)
        print(display_cart())
        print("\nWhat would you like to do?")
        print("1. Return to Main Menu")
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            # Return to main menu
            return
        else:
            clear_screen()
            print("\n❌ Invalid choice!")
            enter_key_wait()