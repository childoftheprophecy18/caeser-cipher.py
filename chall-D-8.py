# Ceaser Cipher
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# TODO 3-1: Combine the encrypt() and decrypt() functions into a single function called caesar()
def caesar(start_text, shift_amount, Cipher_direction):
    end_text = ""
    if Cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:

    #TODO 4 -3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"    
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char    
    print(f"Here's the {direction}d result: {end_text}")

#TODO 4-1: Import and print the logo from cc.py when the program starts. 
from cc import logo
print(logo)    

# TODO 4-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_continue = True
while should_continue:

# TODO 1 - 1 create a fun called 'encrypt' that takes  the 'text' and 'shift' as inputs

# def encrypt(plain_text,shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabwt.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabwt[new_position]
#         cipher_text += new_letter
#     print(f"The encoded texxt is {cipher_text}")    
# TODO 2 - 1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs. 

# def decrypt(cipher_text,shift_amount):
    
# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#     #e.g. 
#     #cipher_text = "mjqqt"
#     #shift = 5
#     #plain_text = "hello"
#     #print output: "The decoded text is hello" 
#     plain_text= ""
#     for letter in cipher_text:
#         position = alphabwt.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabwt[new_position]
#     print(f"the decoded text is {plain_text} ")    


#     # TODO 1 - 2 inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
    # e.g, plain_text = "Hello"
    # shift = 5
    # chpher_text = "mjqqt"
    # print o/p: "the encoded text is mjqqt"  
        
# # TODO 1 - 3 : call the encrypt fun and pass in the user i/p,, we should be able to test a code and encrypt a msg

# #TODO 2-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

    # if direction =="encode":        
    #     encrypt(plain_text=text,shift_amount=shift)  
    # elif direction == "decode":
    #     decrypt(cipher_text=text,shift_amount=shift)

    direction = input("type 'encode' to encrypt and 'decode' for decrypt: \n")
    text = input("Type your message: \n").lower()
    shift =  int(input("Type the shift number: \n"))

    #TODO 4-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    shift = shift % 26

    #TODO 3-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.   
    caesar(start_text=text,shift_amount=shift, Cipher_direction=direction)     

    result = input("type 'yes' if you want to go again otherwise type 'no' \n")

    if result == "no":
        should_continue = False
        print("Good Bye")