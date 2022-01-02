import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#print(paper)

input_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if input_user >= 3 or input_user < 0:
  print("You loose, because of ivalid number.")
else:
  computer_choice = int(random.randint(0,2))
  #print(computer_choice)

  list_images = [rock, paper, scissors]

  print("Your choice:")
  print(list_images[input_user])
  #if input_user == 0:
    #print(rock)
  #elif input_user == 1:
  # print(paper)
  #elif input_user == 2:
    #print(scissors)
  #else:
  # print("You typed an ivalid number. You loose.")
  print("The computer choose..:")
  print(list_images[computer_choice])


  #if computer_choice == 0:
  # print(rock)
  #elif computer_choice == 1:
  # print(paper)
  #else:
  # print(scissors)




  elif input_user == 0 and computer_choice == 1:
    print("You loose.")
  elif input_user == 1 and computer_choice == 1:
    print("It's a draw.")
  elif input_user == 2 and computer_choice == 1:
    print("You win!")
  elif input_user == 0 and computer_choice == 0:
    print("It's a draw.")
  elif input_user == 1 and computer_choice == 0:
    print("You win.")
  elif input_user == 2 and computer_choice == 0:
    print("You loose.")
  elif input_user == 0 and computer_choice == 2:
    print("You win.")
  elif input_user == 1 and computer_choice == 2:
    print("You loose.")
  elif input_user == 2 and computer_choice == 2:
    print("It's a draw.")
