import msvcrt
import os   


def clear_screens():
    """Clear the console screen for better readability."""
    os.system("cls" if os.name == 'nt' else 'clear')

# ============================================================================

# KEY PRESS FUNCTIONS
# ============================================================================

def wait_for_enter():
    # ============================================================================
    # waits for the user to press the Enter key and ignors any other keys and want print any key to the screen
    # ============================================================================
    print()
    print("Press Enter to continue...")
    while True:
        key = msvcrt.getch()
        if key == b'\r':  # Enter key
            break
        # All other keys are ignored (not displayed)

# Use it like this:

# ============================================================================
# CONFIRMATION FUNCTION
# ============================================================================

def wait_for_confirm(message):
    # ============================================================================
    # allows the user to use a yes no confirmation (y/n) and ignores any other keys and want print any key to the screen but can pass a message to the function
    # example : user_choice = wait_for_confirm("Are you sure you want to exit? (y/n): ")
    # ============================================================================
    print()
    print(message)
    while True:
        key = msvcrt.getch()
        if key == b'y':  # y key
            return 'y'

        elif key == b'n':  # n key
            return 'n'
        # All other keys are ignored (not displayed)

# Use it like this:
