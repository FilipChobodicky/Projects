import os

dictionary = {}

print("Welcome to silent-auction program")

lets_continue = "yes"

while lets_continue == "yes":
    name = input("Name: \n")
    offer = int(input("Offer: \n"))
    dictionary[name] = offer
    lets_continue = input("I there any other auditor? Type 'yes' or 'no'")
    if lets_continue == "no":
        os.system("clear")
print(dictionary)

highest_offer = 0
winner = ""
for key in dictionary:
    if dictionary[key] >  highest_offer:
       highest_offer =  dictionary[key]
       winner = key
print(f"Winner of the silent auction is {winner} with offer {highest_offer} USD")
# print(highest_offer)
# print(winner)
     


