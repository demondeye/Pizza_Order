"""
Folder Package Initialization
==============================
This file makes the folder a Python package and exports all menu functions,
cart functions, mains functions, and key press utilities for easy importing.

Author: Your Name
Date: November 2025
Version: 1.0
"""

# ============================================================================
# IMPORTS (Order matters - import dependencies first!)
# ============================================================================

# Import key press functions FIRST (no dependencies)
from .Key_press import wait_for_enter, wait_for_confirm

# Import cart functions SECOND (depends on Key_press)
from .cart import (
    add_item,
    remove_item,
    get_cart,
    get_cart_count,
    get_cart_total,
    clear_cart,
    is_empty,
    display_cart,
    show_cart_menu
)

# Import the cart module itself for use as cart.function()
from . import cart as cart_module
cart = cart_module

# Import mains module and functions THIRD (depends on cart and Key_press)
from . import mains as mains_module
mains = mains_module

from .mains import (
    mains_show_mains,
    display_pizza_menu,
    get_pizza_by_name,
    get_all_pizzas,
    PIZZAS
)

# Import menu functions LAST (depends on cart, mains, and Key_press)
from .menu import (
    display_main_menu,
    get_user_choice,
    show_mains,
    show_sides,
    show_drinks,
    show_dessert,
    show_cart,
    show_invalid_choice,
    show_exit_message,
    clear_screen
)

# ============================================================================
# EXPORTS
# ============================================================================

# Define what gets exported when someone does "from folder import *"
__all__ = [
    # Menu functions
    'display_main_menu',
    'get_user_choice',
    'show_mains',
    'show_sides',
    'show_drinks',
    'show_dessert',
    'show_cart',
    'show_invalid_choice',
    'show_exit_message',
    'clear_screen',
    
    # Cart module and functions
    'cart',
    'add_item',
    'remove_item',
    'get_cart',
    'get_cart_count',
    'get_cart_total',
    'clear_cart',
    'is_empty',
    'display_cart',
    'show_cart_menu',
    
    # Mains module and functions
    'mains',
    'mains_show_mains',
    'display_pizza_menu',
    'get_pizza_by_name',
    'get_all_pizzas',
    'PIZZAS',
    
    # Key press functions
    'wait_for_enter',
    'wait_for_confirm'
]