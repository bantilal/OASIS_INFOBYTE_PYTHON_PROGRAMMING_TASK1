import random
import string


#user input

def get_user_input():
    #ask for password length
    while True:
        length = input('Enter the desired password length : ')
        if length.isdigit() and int(length)>0:
            length = int(length)
            break
        else:
            print("please enter a valid number of greater than 0 . ")
            
    # Ask for character types to include8
    
    include_letters = input("include letters?(y/n) :").lower()=='y'
    include_digits = input("include digits?(y/n) :").lower()=='y'
    include_symbols = input("include symbols?(y/n) :").lower()=='y'
    
    return length,include_letters,include_digits,include_symbols




def generare_password(length,letters,digits,symbols):
    # creating a string of possible characters based on user input
    possible_characters=''
    
    if letters:
        possible_characters+=string.ascii_letters
    if digits:
        possible_characters+= string.digits
    if symbols:
        possible_characters+=string.punctuation
        
    # check if the charactr set is not empty
    if not possible_characters :
        raise ValueError('No character tyoes selected; unable to generate a password.')
    
    #generate the password 
    password =''.join(random.choice(possible_characters) for _ in range(length))
    return password

def main():
    length,letters,digits,symbols = get_user_input()
    print("your password required lenth is ",length)
    
    try:
        password= generare_password(length,letters,digits,symbols)
        print("Generated Password : ",password)
    except ValueError as e:
        print(e)
        
if __name__ =="__main__":
    main()
