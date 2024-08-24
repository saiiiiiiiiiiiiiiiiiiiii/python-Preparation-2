import random

User_wins = 0
Computer_wins = 0
options = ["rock","paper","scissor"]
while True:
  user_input = input('Type Rock/Paper/Sicissor or Quit.').lower()
  if user_input == 'quit':
    print(f"you won {User_wins} times")
    print(f"computer wins {Computer_wins} times")
    print(' Try next time:)')
    quit()
  
  if user_input not in options:
    continue
  random_predection = random.randint(0, 2)
  # rock: 0, paper: 1. sicissor: 2
  computer_pick = options[random_predection]
  print(f"computer_picked ({computer_pick}).")

  if user_input == 'rock' and computer_pick == 'scissor':
    print('You Won!') 
    User_wins = User_wins + 1
    continue
    
  elif user_input == 'paper' and computer_pick == 'rock':
    print('You Won!')
    User_wins = User_wins + 1
    continue
    
  elif user_input == 'scissor' and computer_pick == 'paper':
    print('You Won!')
    User_wins = User_wins + 1
    continue
  else:
    print('You Lost')
    Computer_wins = Computer_wins + 1
  
    print(f"you won {User_wins} times")
    print(f"computer won {Computer_wins} times")
    # print('Goodbye')
