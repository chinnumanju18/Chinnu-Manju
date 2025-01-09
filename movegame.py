def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest. There are paths leading left and right.")
    first_choice()

def first_choice():
    choice = input("Which direction would you like to go? (left/right): ").lower()

    if choice == "left":
        print("You head left and encounter a raging river. You need to cross it.")
        river_choice()
    elif choice == "right":
        print("You walk right and stumble into a clearing with a sleeping dragon!")
        dragon_choice()
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def river_choice():
    choice = input("Do you try to swim across or look for a bridge? (swim/bridge): ").lower()

    if choice == "swim":
        print("The current is too strong, and you are swept away. Game Over.")
    elif choice == "bridge":
        print("You find a bridge and cross safely. You see a mountain ahead.")
        mountain_choice()
    else:
        print("Invalid choice. Please try again.")
        river_choice()

def dragon_choice():
    choice = input("Do you try to sneak past the dragon or fight it? (sneak/fight): ").lower()

    if choice == "sneak":
        print("You successfully sneak past the dragon and find a treasure chest. You Win!")
    elif choice == "fight":
        print("The dragon wakes up and breathes fire. Game Over.")
    else:
        print("Invalid choice. Please try again.")
        dragon_choice()

def mountain_choice():
    choice = input("Do you climb the mountain or walk around it? (climb/around): ").lower()

    if choice == "climb":
        print("You reach the top and enjoy a breathtaking view. You find a hidden path leading to safety. You Win!")
    elif choice == "around":
        print("You get lost while walking around the mountain. Game Over.")
    else:
        print("Invalid choice. Please try again.")
        mountain_choice()

# Start the game
start_game()
