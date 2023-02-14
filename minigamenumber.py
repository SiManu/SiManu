import random

attempts_list = []


def show_score():
  if not attempts_list:
      print('Não há nenhuma pontuação.''É sua vez de pontuar!')

  else:
      print(f'A pontuação mais alta foi {min(attempts_list)} tentativas')


def start_game():
   attempts = 0
   rand_num = random.randint(1, 10)
   print('Olá viajante, esse é o jogo de advinhação')
   player_name = input('Qual é o seu nome? ')
   wanna_play = input(
       f'Oi, {player_name}, gostaria de jogar o jogo da advinhação?'
       '(Digite Sim/Não): ')

   if wanna_play.lower() != 'sim':
      print('Poxa que pena.')
      exit()
   else:
       show_score()

   while wanna_play.lower() == 'sim':
       try:
           guess = int(input('Escolha um número de 1 a 10: '))
           if guess < 1 or guess > 10:
               raise ValueError(
                   'Por favor, escolha um valor dentro da escala.')

           attempts += 1
           attempts_list.append(attempts)

           if guess == rand_num:
               print('Boa! Você acertou!')
               print(f'Você levou {attempts} tentativas.')
               wanna_play = input(
                   'Gostaria de jogar de novo? (Digite Sim/Não): ')
               if wanna_play.lower() != 'sim':
                   print('Poxa que pena.')
                   break
               else:
                   attempts = 0
                   rand_num = random.randint(1, 10)
                   show_score()
                   continue
           else:
               if guess > rand_num:
                   print('É menor!')
               elif guess < rand_num:
                   print('É maior!')

       except ValueError as err:
           print('ERROR, você tentou um valor não condizente com as regras, tente novamente')
           print(err)


if __name__ == '__main__':
   start_game()





