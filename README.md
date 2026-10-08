# Structured Programming Adventure Game

Create a text-based adventure game in Python. Your game will use a **state machine** to move the player between different rooms or locations. You may choose any theme you want, such as fantasy, science fiction, mystery, school, survival, comedy, or something completely original.

Whenever the player enters a room, the program should provide a brief description of the location and present the actions that are currently available. The player will interact with the game by entering text commands or selecting from a numbered list of choices.

For example:

```text
You wake up in a square torchlit room.
You feel the warm cracked stone tile beneath you as you come to your senses.
A small brass key lies on an ornate stone pedestal.
In the center of each wall is a door with a keyhole.

What would you like to do?
1. Take Key
2. Try North Door
3. Try East Door
4. Try South Door
5. Try West Door
```

As the player completes actions, the game should remember what has happened and change accordingly.

## Project Requirements Checklist

* [ ] Game uses a state machine with a minimum of 10 states to represent "rooms".
* [ ] State machine is non-linear allowing players to return to previous states.
* [ ] Clear prompts are provided in each room to the player indicating what actions they can take and what input they need to provide to take such actions.
* [ ] State machine is controlled by text input from a player.
* [ ] The player can successfully complete the game by getting to an end point or win state.
* [ ] A minimum of 6 variables are used to track other game information (this could be things like collected items, NPCs that a player has met, or locked doors, etc.).
* [ ] At least 1 prompt provided to the player changes depending on at least one of the aforementioned variables (for example: If they have do not have a key when they enter a room, they do not have the option to go through a locked door. If they do have a key, the prompt changes to allow them to go through the locked door.)
* [ ] At least 1 "puzzle input" that requires the player to provide a specific input to get past the obstacle (this could be a password hidden elsewhere in the game, the solution to a riddle or math problem, or the solution to a puzzle of your creation).
* [ ] Input is always verified before the program can continue (this includes creating a loop that does not exit until the input is validated AND providing the player a clear message about why their input was invalid).
* [ ] The game does not produce any errors and does not crash.
* [ ] Python code follows the Best Practices provided by Mr. Forsyth.

### Demonstrate Structured Programming:

* [ ] **Sequence:** Instructions are organized in a logical order so that actions happen at the correct time.
* [ ] **Selection:** `if`, `elif`, and `else` statements are used to make decisions based on user choices and the current state of the game.
* [ ] **Iteration:** Loops are used appropriately to repeat gameplay and/or validate user input.
* [ ] **Functions:** Functions are used to organize the program into manageable sections and avoid unnecessary repeated code.

## What "Changing Options" Looks Like

Consider the following example of what it might look like for a players options to change over the course of the game.

### It Could Be That Actions In The Room Change The Room

The first time they enter a room their options might be:

```text
You enter a small room.
Inside the room is a locked trunk marked with your initials.

1. Use key on trunk.
2. Leave room.
```

Then if the player uses the key on the trunk in the room, and leave and come back later, they might receive a different message:

```text
You enter a small room.
Inside the room is an open trunk that used to contain your family's crown.

1. Close trunk.
2. Leave room.
```

### It Could Be That Actions in One Room Affect Another Room

Consider you enter a room for the first time and get this message:

```text
In front of you lies what appears to be a fountain, but with no running water.
To the south is a door where you can hear a small dripping sound.
To the west is a well lit hallway.

1. Inspect fountain
2. Go south
3. Go west
```

Perhaps in the south room there is a lever that the player can pull, which activates the fountain. When they return to the fountain room, the player may get a different message:

```text
The fountain flows with a sparkling liquid that looks almost like flowing gold.
There is a door to the south, but the small dripping sound has stopped.
To the west is a well lit hallway.

1. Inspect fountain
2. Drink from fountain
3. Go south
4. Go west
```

## Creativity

The requirements above describe the minimum functionality your game must include. Everything else is up to you.

You are encouraged to create your own setting, characters, story, puzzles, obstacles, items, secrets, and game mechanics. Your game can be serious, funny, strange, challenging, story-focused, or anything else you would enjoy creating, as long as it meets all of the project requirements.

## CSE 1110 - Structured Programming 1

| Outcome                                 | Excellent                                                                                                                                                                                            | Proficient                                                                                                                                                       | Developing                                                                                                                                             | Emerging                                                                                                                                             |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input and Output                        | Program uses input and output effectively throughout the game, with clear prompts and highly effective feedback that makes the game easy to understand and navigate.                                 | Program uses user input appropriately and consistently displays clear, relevant output that communicates the state of the game.                                  | Program generally uses user input and output appropriately, but some interactions may be unclear or inconsistent.                                      | Program uses user input or displays output, but input/output may be incomplete, unclear, or inappropriate for the game.                              |
| Variables and Data Types                | Program uses variables and data types deliberately and efficiently, with clear variable names and effective choices for representing different kinds of game information.                            | Program uses appropriate variables and data types to store and process the information needed by the game.                                                       | Program uses variables to store game information, but variable choices, data types, or usage may sometimes be inefficient or unclear.                  | Program uses few variables, or variables are used incorrectly or do not effectively represent game information.                                      |
| Sequence Control Structures             | Program demonstrates strong control over sequence, with functions and instructions organized into a clear, intentional, and easy-to-follow program flow.                                             | Program is effectively structured so instructions execute in a clear and logical sequence.                                                                       | Program generally follows a logical sequence, but some sections could be organized more effectively.                                                   | Program execution is difficult to follow or instructions frequently occur in an inappropriate order.                                                 |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements                    | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the game.                                           | All requirements outlined in the project description are successfully implemented.                                                                               | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently.                                      | Several major requirements from the project description are missing or incomplete.                                                                   |

## CSE 1120 - Structured Programming 2

| Outcome                                 | Excellent                                                                                                                                                                                            | Proficient                                                                                                                                                       | Developing                                                                                                                                             | Emerging                                                                                                                                             |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input Validation                        | Program consistently and efficiently validates input throughout the game, providing clear feedback and allowing the player to recover easily from invalid entries.                                   | Program validates user input before continuing and handles invalid input without crashing or producing unexpected behaviour.                                     | Program validates some user input, but validation may be inconsistent or may not account for all expected invalid inputs.                              | User input is frequently used without validation, and invalid input may cause errors or unexpected behaviour.                                        |
| Selection Control Structures            | Program uses selection control structures deliberately and efficiently to manage complex game decisions and changing game states while keeping the code clear and understandable.                    | Program effectively uses selection control structures to make decisions based on user input and the current state of the game.                                   | Program uses `if`, `elif`, and/or `else` structures appropriately in most situations, but some decisions may be inefficient or unclear.                | Selection structures are missing, frequently incorrect, or do not effectively control program behaviour.                                             |
| Iteration Control Structures            | Program uses iteration control structures deliberately and efficiently, minimizing unnecessary repetition while maintaining clear and predictable program flow.                                      | Program effectively uses iteration control structures to manage repeated gameplay, input validation, and other repeated processes.                               | Program uses loops for some appropriate tasks, but iteration may be inconsistent, inefficient, or unnecessarily repetitive.                            | Loops are missing, frequently incorrect, or do not effectively control repeated program behaviour.                                                   |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements                    | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the game.                                           | All requirements outlined in the project description are successfully implemented.                                                                               | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently.                                      | Several major requirements from the project description are missing or incomplete.                                                                   |

