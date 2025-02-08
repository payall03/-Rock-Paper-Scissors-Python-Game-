print('''

█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
''')
Rock= ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
Paper = (''' 
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
Scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
import random
print("Enter 0 for Rock and 1 for Paper and 2 for Scissor:")
user_choice = int(input())
print("you chose:",user_choice)
if user_choice == 0:
    print(Rock)
elif user_choice == 1:
    print(Paper)
elif user_choice == 2:
    print(Scissor)
else:
    print("Invalid number")
computer_choice = random.randint(0,2)
print("Computer Choose",computer_choice)
if computer_choice == 0:
    print(Rock)
elif computer_choice == 1:
    print(Paper)
elif computer_choice == 2:
    print(Scissor)
else:
    print("Invalid number")

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice ==1:
    print("You lose")
elif user_choice ==0 and computer_choice ==2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 1 and computer_choice ==2:
    print("You lose")
elif user_choice == 2 and computer_choice ==0:
    print("You lose")
elif user_choice == 2 and computer_choice ==1:
    print("You win")
else:
    print("Game Over")
print("Thank you for playing")