import os


def sum(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    '''Scitani'''
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': sum,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input('Jake je prvni cislo? '))

    lets_continue = 'ano'

    while lets_continue == 'ano':
        for symbol in operations:
            print(symbol)

        user_symbol = input('Zvolte jednu operaci: ')
        num2 = float(input('Jake je druhe cislo? '))

        calc_function = operations[user_symbol]
        result = calc_function(num1, num2)

        print(f'{num1} {user_symbol} {num2} = {result}')
        lets_continue = input(
            'Napiste ano pro pokracovani nebo ne pro znovuspusteni: ')
        if lets_continue == 'ano':
            num1 = result
        else:
            os.system('clear')
            calculator()


calculator()
