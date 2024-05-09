def exploreRoom():
    description = "You are in a room. You can see a door."
    print(description)

    action = input("What would you like to do? (open door/close door): ")

    if action.lower() == "open door":
        print("You opened the door and found a key.")
        print("You win!")  # In a real game, you would navigate to the next room
    elif action.lower() == "close door":
        print("You closed the door.")
    else:
        print("Invalid action.")

if __name__ == "__main__":
    exploreRoom()
