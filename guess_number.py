import random
import os

print('Vitejte ve hre guess secret number')
print('Myslim si cisl od 1 do 100')


def difficulty():
    difficulty = input('Vyberte obtiznost easy nebo hard: ')
    if difficulty == 'easy':
            return 10
    elif difficulty == 'hard':
            return 5

def guess_game():
    secret_number = random.randint(1, 100)

    attempts = difficulty()
    another_game = ''

    while attempts > 0:
        print(f'Pocet zbyvajicich pokusu je {attempts}')
        guess = int(input('Typni si cislo: '))
        if guess < secret_number:
            print('Prisli nizke')
            attempts -= 1
        elif guess > secret_number:
            print('Prilis vysoke')
            attempts -= 1
        else:
            print('Vyhral jsi, PC porazen!')
            another_game = input('Napis "yes" pro pokracovani a nebo "no" pro ukonceni: ')
        
        if attempts == 0:
            print('Prohral jsi, PC vyhral')
            another_game = input(
                'Napis "yes" pro pokracovani a nebo "no" pro ukonceni')
        
        if another_game == 'yes':
            os.system('clear')
            guess_game()
        elif another_game == 'no':
            os.system('clear')
            break

guess_game()
