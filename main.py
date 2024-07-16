import random
from art import logo
import os

print(logo)

#selects the random number from 1 - 100.
num = random.randint(1,100)
level = input("Choose the level of the game, 'HARD' or 'EASY': ")
os.system('cls')

#if the user chooses "HARD" then 5 lives will be given and in "EASY" 5 lives will be given. 
if level == "HARD":
  lives = 5
  print(f"You have {lives} lives.")
elif level == "EASY":
  lives = 10
  print(f"You have {lives} lives.")
else:
  print("INVALID INPUT!.")


#actual game, when the num is low then guess it shows too low and if it is high then it shows too high.
#each wrong input the user looses 1 life and if the 0 lives are left the user looses the game.
while lives > 0:
  guess = int(input("\nGuess the number: "))

  if guess == num:
    print(f"You guessed it correct. {num}")
    lives = -1
  elif guess > num:
    print("Too high")
    lives -= 1
    print(f"Lives left: {lives}")
  elif guess < num:
    print("Too low") 
    lives -= 1
    print(f"Lives left: {lives}")

if lives == 0:
  print(f"\nYou loose the number was {num}.")

