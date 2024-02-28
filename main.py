from art import logo
from art import vs
import random
from game_data import data
from replit import clear
print(logo)
option_A = (random.choice(data))
option_B = (random.choice(data))
final_score = 0
game_on = True
while game_on == True:
  print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}.")
  print(vs)
  print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}.")
  answer = input("\nWho has more followers? Type 'A' or 'B' :\n")
  clear()
  if answer == "A":
    choice = option_A
    choice_followers = choice['follower_count']
  elif answer == "B":
    choice = option_B
    choice_followers = choice['follower_count']
  else:
    print("Error! Wrong input!")
  followers_pool = [option_A['follower_count'], option_B['follower_count']]
  if choice_followers >= max(followers_pool):
    final_score += 1
    print(logo)
    print(f"You're right!. Current score: {final_score}")
    game_on = True
    option_A = choice
    option_B = (random.choice(data))
  elif choice_followers < max(followers_pool):
    game_on = False
if game_on == False:
  print(logo)
  print(f"Sorry, that's wrong. Final score: {final_score}")
