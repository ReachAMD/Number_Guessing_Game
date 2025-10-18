#  Number Guessing Game (Python)

A simple and interactive command-line **Number Guessing Game** built
using Python fundamentals.\
The program randomly selects a number between **1 and 100**, and the
player must guess it.\
After each guess, the program provides hints until the correct number is
guessed.

------------------------------------------------------------------------

##  Features

-   Generates a random number between 1 and 100\
-   Gives feedback on whether your guess is **too high** or **too low**\
-   Tracks the **number of attempts**\
-   Handles invalid inputs gracefully\
-   Built entirely using Python's standard library (no external
    dependencies)

------------------------------------------------------------------------

##  How to Run

1.  **Clone this repository:**

    ``` bash
    git clone https://github.com/yourusername/number-guessing-game.git
    ```

2.  **Navigate to the project folder:**

    ``` bash
    cd number-guessing-game
    ```

3.  **Run the script:**

    ``` bash
    python number_guess.py
    ```

    > Make sure you have Python 3 installed on your system.

------------------------------------------------------------------------

##  Example Gameplay

    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100. Can you guess it?
    Enter your guess: 50
    Too low! Try again.
    Enter your guess: 75
    Too high! Try again.
    Enter your guess: 63
    Congratulations! You guessed the number 63 in 3 attempts.

------------------------------------------------------------------------

##  Code Overview

The game logic is implemented in the function `random_number_guess()`:

-   Uses `random.randint(1, 100)` to generate the secret number\
-   Accepts user input with proper error handling using `try/except`\
-   Provides hints and counts total attempts\
-   Displays a congratulatory message upon a correct guess

``` python
if __name__ == "__main__":
    random_number_guess()
```
