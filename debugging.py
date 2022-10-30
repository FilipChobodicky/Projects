# Popiš problém ########
# def test_function():
#   for number in range(1, 10):
#     if number == 10:
#       print("Vše je správně")
# test_function()

#debug  #########
# def test_function():
#   for number in range(1, 11):
#     if number == 10:
#       print("Vše je správně")
# test_function()



# Občas funguje a občas ne #######
# import random
# all_dice_numbers = ["1", "2", "3", "4", "5", "6"]
# dice_number = random.randint(1, 6)
# print(all_dice_numbers[dice_number])

# #debug  #########

# import random
# all_dice_numbers = ["1", "2", "3", "4", "5", "6"]
# dice_number = random.randint(0, 5)
# print(all_dice_numbers[dice_number])



# Mysli jako počítač ###############
# year = int(input("Jaký je váš rok narození?"))
# if year > 1980 and year < 1994:
#   print("Jste millenial.")
# elif year > 1994:
#   print("Jste generace Z.")

# # #debug  #########

# year = int(input("Jaký je váš rok narození?"))
# if year > 1980 and year < 1994:
#   print("Jste millenial.")
# elif year >= 1994:
#   print("Jste generace Z.")



# Oprav hned chyby ####################
# age = input("Kolik je vám let?")
# if age > 18:
#     print("Ve věku {age} můžete kupovat alkohol.")

# # #debug  #########

# age = int(input("Kolik je vám let?"))
# if age > 18:
#     print(f"Ve věku {age} můžete kupovat alkohol.")

# najdi chybu ########################
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print("number")

# debug ###################

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)
