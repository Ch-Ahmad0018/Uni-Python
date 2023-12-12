import random
# def guess_Number():
#      target_number=random.randint(1,100)

#      print("Welcome to the Number Guessing Game!")
#      print("Guess the number between 1 and 100.")

#      attempts=0

#      while True:
#          guess=int(input("Enter your guess"))
#          attempts+=1

#          if(guess==target_number):
#              print(f"U have guessed the right number {guess_Number} in {attempts} attempts")
#              break
#          elif guess<target_number:
#              print("Number is too low")

#          else:
#              print("Number is too high")  


# guess_Number()      
        
# import random

# def number_guessing_game():
#     # Generate a random number between 1 and 100
#     target_number = random.randint(1, 100)

#     print("Welcome to the Number Guessing Game!")
#     print("Guess the number between 1 and 100.")

#     attempts = 0

#     while True:
#         # Get the player's guess
#         guess = int(input("Enter your guess: "))
#         attempts += 1

#         # Check if the guess is correct
#         if (guess == target_number):
#             print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
#             break
#         elif (guess < target_number):
#             print("Too low. Try again.")
#         else:
#             print("Too high. Try again.")

# # Play the number guessing game
# number_guessing_game()

def number_guess():
    targetNumber=random.randint(1,100)
    attempts=0
    print("Welcom to game")
    while True:
        guess=int(input("Enter your guess"))
        attempts+=1
        if(guess==targetNumber):
            print(f"You have guess the number {targetNumber} in {attempts} attempts")
            break
        elif (guess<targetNumber):
            print("Number is too low")
        else:
            print("Number is too high")

number_guess()
