import random

print("Hola! Bienvenido a Piedra, Papel o Tijera!!")
user_name = input('¿Cuál es tu nombre? >> ')
print('Encantado',user_name,)
print('Tu rival será Leia, nuestra mejor jugadora!')
print('-' * 43)
print('Comencemos!! - Recordamos que solo debe elegir una opción.')

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('Esa opción no es válida')
    return None, None
    
  computer_option = random.choice(options)

  print('Tu opción =>', user_option)
  print('Opción de Leia =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('Has sumado un punto!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Punto para Leia!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('Has sumado un punto!')
      user_wins += 1
    else:
      print('Tijera gana a papel')
      print('Punto para Leia!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('Has sumado un punto!')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('Punto para Leia!')
      computer_wins += 1
  return user_wins, computer_wins


def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 8)
    print('ROUND', rounds)
    print('*' * 8)

    print('Puntos de Leia:', computer_wins)
    print('Tus puntos', user_wins)
    print('~'*18)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 3:
      print('Lo sentimos, no has podido ganarle a Leia. No te rindas!')
      break

    if user_wins == 3:
      print('En hora buena, le has ganado a nuestra mejor jugadora!')
      break

run_game()
