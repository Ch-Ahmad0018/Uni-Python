#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#else if


# In[ ]:


#Example1: Temperature Classifier


# In[1]:


# Program to classify temperature into different categories
# temperature = float(input("Enter the temperature in Celsius: "))

# if temperature < 0:
#     print("It's freezing!")
# elif temperature>=0 and temperature<=10:
#     print("It's cold.")
# elif temperature>10 and temperature<=20:
#     print("It's cool.")
# elif 20 < temperature <= 30:
#     print("It's warm.")
# else:
#     print("It's hot!")


# In[ ]:


#Example 2: Grade Classifier


# In[2]:


# Program to classify grades based on score
# score = int(input("Enter your score: "))

# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score < 90:
#     grade = 'B'
# elif 70 <= score < 80:
#     grade = 'C'
# elif 60 <= score < 70:
#     grade = 'D'
# else:
#     grade = 'F'

# print(f"Your grade is: {grade}")


# In[ ]:


import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    attempts = 0

    while True:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == target_number:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

# Play the number guessing game
number_guessing_game()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




