import random

def random_number_guess():
    #Generate a random number between 0 and 100
    secret_number = random.randint(1,100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            #Get User Input
            guess = int(input("Enter your guess: "))
            attempts += 1

            #Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    random_number_guess()

