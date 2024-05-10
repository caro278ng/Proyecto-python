import random
options = ('piedra', 'papel', 'tijeras')

print('*'*35)
print('BIENVENIDO A PIEDRA, PAPEL O TIJERAS')
print('*'*35)

computer_wins = 0
user_wins = 0

rounds = 1

while True:

  print('*'*10)
  print('ROUND', rounds)
  print('*'*10)
  print('')
  print('computers wins', computer_wins)
  print('user wins', user_wins)
  print('')

  user_option_input = input('Elige piedra, papel o tijeras => ')
  user_option = user_option_input.lower()
  computer_option = random.choice(options)

  if not user_option in options: 
    print('Opción no válida')
    continue

  print("")
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  print("")

  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijeras':
      print('Piedra gana a tijeras')
      print('User ganó!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Computer ganó!')
      computer_wins += 1

  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('User ganó!')
      user_wins += 1
    else: 
      print(f'Tijeras gana a {user_option}')
      print('Computer ganó!')
      computer_wins += 1

  elif user_option == "tijeras":
    if computer_option == "papel": 
      print(f"{user_option} gana a {computer_option}")
      print("User ganó!")
      user_wins += 1
    else:
      print(f"piedra gana a {user_option}")
      print('Computer ganó!')
      computer_wins += 1


  if computer_wins == 2: 
    print('')
    print('El ganador es la computadora')
    break

  if user_wins == 2:
    print('')
    print('El ganador es el usuario')
    break

  rounds += 1