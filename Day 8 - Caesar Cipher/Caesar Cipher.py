import os

letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h','i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

def caesar(message, shift, task):
    if task == "decode":
        shift *= -1
    
    cipher = ""
    
    for c in message:
        if c not in letters:
            cipher += c
            continue
        letter_id = letters.index(c)
        shifted_letter_id = (letter_id + shift) % 26
        cipher += letters[shifted_letter_id]
    
    if task == "encode":
        print(f"Here's your encoded result: {cipher}\n")
    else:
        print(f"Here's your decoded result: {cipher}\n")
    
    

while True:
    task = input("Type 'encode' to encrypt, 'decode' to decrypt, 'q' to quit:\n").lower()
    
    if task == 'q':
        os.system('cls')
        break
    
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar(message, shift, task)
        