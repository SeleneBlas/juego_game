import random

print("Hi! Welcome to Rock Paper Scissors")
user_name = input("What is your name? >> ")
print('Pleased to meet you',user_name,)
print("Lets's start with the game. You will play vs our best player")
print('-' * 43)
print('Play! Remember that you have to choose one opition')

def choose_options():
  options = ('rock', 'paper', 'scissors')
  user_option = input('rock, paper or scissors => ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('that option is not valid')
    return None, None
    
  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Tie!')
  elif user_option == 'rock':
    if computer_option == 'scissors':
      print('rock break scissors')
      print('user wins!')
      user_wins += 1
    else:
      print('paper covers rock')
      print('computer wins!')
      computer_wins += 1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('paper covers rock')
      print('user wins')
      user_wins += 1
    else:
      print('scissors cuts paper')
      print('computer wins!')
      computer_wins += 1
  elif user_option == 'scissors':
    if computer_option == 'paper':
      print('scissors cuts paper')
      print('user wins!')
      user_wins += 1
    else:
      print('rock break scissors')
      print('computer wins!')
      computer_wins += 1
  return user_wins, computer_wins


def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    print('~'*18)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('The winner is... Computer :(')
      break

    if user_wins == 2:
      print('The winner is... User!!')
      break

run_game()