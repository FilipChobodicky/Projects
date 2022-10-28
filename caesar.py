alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift_number):                  # jake promenne budeme ve funkci pouzivat. Dostaneme message = slovo a budeme ho posouvat = shift_number. Toto musi byt pak ve volani funkci
    shifted_text = ""
    for one_letter in message:                      #z message = zadane jmeno posli kazde pismenko do one_letter
        if one_letter != " ":                       # pokud bude v message zadana mezera (napr. Ahoj Lenko)
            index = alphabet.index(one_letter)      # z nelezenoho pismenka v one_letter mi napis jaky ma index 
            new_index = index + shift_number        # v sifre se index napsaneho pismene posune o index zadaneho cisla shift_number
            shifted_text += alphabet[new_index]     # do shifted_text pridat z alphabetu to co ma index new_index
        else:
            shifted_text += one_letter              # pokud to je mezera, pridej to rovnou do shifted_text
    print(f" Your code is: {shifted_text}")



def decode(encrypted_message, shift_number):
    normal_text = ""
    for one_letter in encrypted_message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index - shift_number
            normal_text += alphabet[new_index]
        else:
            normal_text += one_letter
    print(normal_text)



lets_continue = "yes"

while lets_continue == "yes":
    direction = input("Write 'encode' if you want to encode the message. Write 'decode' if you want to decode the message.\n")
    text  = input("Write your message:\n").lower()  
    shift = int(input("Write change number:\n"))

    if direction == "encode":
        encode(text, shift)
        lets_continue = input("Write 'yes' if you want to continue. Write 'no' if you want to quit program\n")
    elif direction == "decode":
        decode(text, shift )
        lets_continue = input("Write 'yes' if you want to continue. Write 'no' if you want to quit program\n")
    else:
        print("Invalid operation")

else:
    print("Thank you for using our encryption program")

