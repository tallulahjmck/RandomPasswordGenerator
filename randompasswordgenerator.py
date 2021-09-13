import random
##imports the random library
##allows us to pick characters randomly from our chars variable in this case

def main():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@$%^&*'
    
##assigning our characters to the variable chars
##essentially storing this data to access later on :-)
    
    number = input('Number of passwords? - ')
    number = int(number)
    
##we need to ask the user how many passwords they want to generate
##then we're going to store that number as an integer in the variable number
    
    length = input('Password length? - ')
    length = int(length)
    
##we need to ask the user how long they want their password to be
##then we're going to store that length in the variable length

    for p in range(number):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(password)
        
##first we need to get the number the user entered
##we need the range function so we can loop through however many times the user entered 
##then we need to store the characters in the variable password
##next we need to see how long the user wanted their password(s) to be 
##+= adds another value with the variable's value
##next we need to print the users new password!

    print('. . . . . PASSWORD(S) GENERATED SUCCESSFULLY . . . . .')
    yn = input('Press the Y key to go back to the start of the program or N to exit... ')
    if yn == 'Y':
        main() 
    elif yn == 'N':
        exit()
        
##we have printed a nice statement to show when the passwords have finished
##next we have a simple elif statement based on user input Y/N to repeat or exit the program
##we have our code within our main function, which means that we can loop back nicely to the start where we declared it

main()
