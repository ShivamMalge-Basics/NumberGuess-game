import random
print("Welcome to the number guessing game!")

def number_select():
    secret_number = random.randint(1, 100)
    return secret_number

print("I am thinking of a number from 1 to 100")
secret_number = number_select()

# Choose difficulty
total_attempts = 0 
difficulty = input("Choose difficulty: 'easy' or 'hard': ").lower()

if difficulty == "easy":
    total_attempts = 10
elif difficulty == "hard":
    total_attempts = 5
else:
    print("Invalid difficulty selected. Defaulting to 'easy'.")
    total_attempts = 10

# Guessing loop
while total_attempts > 0:
    print(f"\nYou have {total_attempts} attempts remaining.")
    user_guess = int(input("Make a guess: "))

    if user_guess > secret_number:
        print("Too high!")
    elif user_guess < secret_number:
        print("Too low!")
    else:
        print(f"You got it! The number was {secret_number}.")
        break  # Ends the loop if guessed correctly

    total_attempts -= 1

if total_attempts == 0:
    print(f"\nYou've run out of guesses. The number was {secret_number}.")
