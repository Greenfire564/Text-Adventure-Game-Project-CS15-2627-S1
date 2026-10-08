def get_valid_choice(prompt: str, valid_choices: list) -> str:
    """Makes the player give a choice that works. Repeats until given.

    :param prompt: Message is given to the player
    :param valid_choices: The list of choices given to the player
    :return: The player input string
    """
    while True:
        user_input = input(prompt)
        if user_input in valid_choices:
            return user_input
        print(f"Invalid choice. Please enter one of the following: {valid_choices}\n")


def solve_lab_puzzle() -> bool:
    """Gives a math puzzle to the player.

    :return: True if the player gives the correct answer in 3 attempts, False otherwise
    """
    print("\nComputer Terminal Puzzle")
    print("To bypass the security, solve this equation:")
    print("What is 5 + 3 * 4?")
    attempts = 0
    while attempts < 3:
        ans = input("Enter the  answer: ")
        if ans == "17":
            print("Access Granted - Security override code has been given to you.")
            return True
        else:
            attempts += 1
            print(f"Incorrect answer. Attempts remaining: {3 - attempts}")
    print("Lockout triggered, Returning to main room menu.")
    return False


def main() -> None:
    """Runs the main game on loop.

    :return: None
    """
    current_room = "hallway"
    game_over = False

    has_keycard = False
    has_flashlight = False
    has_passcode = False
    generator_active = False
    security_bypassed = False
    escaped = False

    while not game_over:
        if current_room == "hallway":
            print("\nCentral Hallway")
            print("You are in the central hallway. Doors lead in all directions.")
            options = ["1", "2", "3", "4"]
            print("1. Go North to Security Post")
            print("2. Go East to Storage Room")
            print("3. Go South to Main Exit")
            print("4. Go West to Laboratory")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                current_room = "security"
            elif choice == "2":
                current_room = "storage"
            elif choice == "3":
                current_room = "exit_gate"
            elif choice == "4":
                current_room = "lab"

        elif current_room == "storage":
            print("\nStorage Room")
            print("A dusty room filled with old crates.")
            options = ["1", "2"]
            if not has_flashlight:
                print("1. Search crates (Looks dark inside)")
            else:
                print("1. Search crates (Search completed)")
            print("2. Return to Central Hallway")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                if not has_flashlight:
                    print("You found a working Flashlight among the crates!")
                    has_flashlight = True
                else:
                    print("You have already searched the crates. There is nothing else here.")
            elif choice == "2":
                current_room = "hallway"

        elif current_room == "lab":
            print("\nLabortory")
            print("A high-tech lab with scientific instruments and terminal screens.")
            options = ["1", "2", "3"]
            print("1. Go to Power Room")
            print("2. Interact with Computer Terminal")
            print("3. Return to Central Hallway")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                current_room = "power_room"
            elif choice == "2":
                if not has_passcode:
                    if solve_lab_puzzle():
                        has_passcode = True
                else:
                    print("You have already bypassed this computer terminal.")
            elif choice == "3":
                current_room = "hal lway"

        elif current_room == "power_room":
            print("\nPower Room")
            print("Large electrical generators loom before you.")
            options = ["1", "2"]
            if not generator_active:
                print("1. Turn on Main Generator Switch")
            else:
                print("1. Main Generator is running")
            print("2. Return to Laboratory")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                if not generator_active:
                    print("You pull the heavy lever. Power is restored to the facility!")
                    generator_active = True
                else:
                    print("The generator is already running smoothly.")
            elif choice == "2":
                current_room = "lab"

        elif current_room == "security":
            print("\nSecurity Room")
            print("Monitoring screens flicker on the wall. Doors connect to other sectors.")
            options = ["1", "2", "3", "4"]
            print("1. Go to Armory")
            print("2. Go to Server Room")
            print("3. Search Security Desk")
            print("4. Return to Central Hallway")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                current_room = "armory"
            elif choice == "2":
                current_room = "server_room"
            elif choice == "3":
                if not has_keycard:
                    print("You open a drawer and find an Executive Keycard!")
                    has_keycard = True
                else:
                    print("The desk drawer is empty.")
            elif choice == "4":
                current_room = "hallway"

        elif current_room == "armory":
            print("\nArmory")
            print("Lockers line the walls in this secure containment zone.")
            options = ["1", "2"]
            print("1. Search Lockers")
            print("2. Return to Security Post")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                if not has_flashlight:
                    print("It is too dark in the corners to safely search the lockers. You need a light source!")
                else:
                    print("Using your Flashlight, you inspect the lockers. You find emergency supplies!")
            elif choice == "2":
                current_room = "security"

        elif current_room == "server_room":
            print("\nServer Rom")
            print("Racks of servers hum loudly. A door leads deeper into the facility.")
            options = ["1", "2", "3"]
            print("1. Go to Control Room")
            print("2. Inspect Server Racks")
            print("3. Return to Security Post")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                current_room = "control_room"
            elif choice == "2":
                if generator_active:
                    print("Power is active. The server indicators are blinking green.")
                else:
                    print("The servers are dark and powered off.")
            elif choice == "3":
                current_room = "security"

        elif current_room == "control_room":
            print("\nControl Room=")
            print("A massive console overlooks the entire facility.")
            options = ["1", "2"]
            print("1. Activate Main Override Console")
            print("2. Return to Server Room")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                if not generator_active:
                    print("The console lacks power. Restore power first!")
                elif not has_passcode:
                    print("Access denied. Security override code missing from Laboratory terminal.")
                else:
                    print("Override successful! Security lockdown disengaged.")
                    security_bypassed = True
            elif choice == "2":
                current_room = "server_room"

        elif current_room == "exit_gate":
            print("\nExit Gate1")
            print("A heavy door blocks the exit to freedom.")
            options = ["1", "2"]
            print("1. Use Keycard on Lock Mechanism")
            print("2. Return to Central Hallway")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                if not has_keycard:
                    print("The door requires an Executive Keycard.")
                elif not security_bypassed:
                    print("Keycard recognized, but security lockdown is still active!")
                else:
                    print("Keycard accepted!")
                    current_room = "courtyard"
            elif choice == "2":
                current_room = "hallway"

        elif current_room == "courtyard":
            print("\nOutside")
            print("You have made it outside!")
            options = ["1"]
            print("1. Walk to the Rescue Helicopter")

            choice = get_valid_choice("Choose an action: ", options)
            if choice == "1":
                escaped = True
                game_over = True

    if escaped:
        print("You successfully escaped!")

if __name__ == "__main__":
    main()