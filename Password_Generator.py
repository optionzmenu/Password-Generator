import random
import string
yes = ["y", "yes"]
no = ["n", "no"]
Or = ("o", "or")

print("PASSWORD CREATOR!")
print("1. Generate a Password based on length (Recommended)")
print("2. Create A Custom Password (Advanced)")

def startprogram():
    while True:
        try:
            response = int(input("Enter Your Selection:"))
            if response == 1:
                generatepassword()
            elif response == 2:
                advancedpassword()
            else:
                print("Please enter a number")
                continue
        except ValueError: 
            print("Wrong input")

def yesorno():
    while True:
        try:
            answer = input("Yes or No?").lower()
        except ValueError:
            print("Wrong input")
        if answer in yes:
            return True
        elif answer in no:
            return False
        elif answer in Or:
            print ("Very Funny!")
            continue
        else:
            print("Did you read the question?")
            continue

def keepgenerating():
    print("\nKeep creating passwords?")
    answer = yesorno()
    if answer is True:
        generatepassword()
    else: 
        exit()

def generatepassword():
    characters = list(string.ascii_letters + string.digits + string.punctuation)

    while True:
        try:
            length = int(input("Enter password length: "))

            random.shuffle(characters)
            
            password = []
            for number in range(length):
                password.append(random.choice(characters))

            random.shuffle(password)

            print("".join(password))

            keepgenerating()

        except ValueError:
            print("\nPlease enter an integer!\n")

def advancedpassword():
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = (string.punctuation)
    characters = list(string.ascii_letters + string.digits + string.punctuation)

    while True:
        try:
            length = int(input("Enter password length: "))

            ## number of character types
            alphabets_count = int(input("Enter alphabets count in password: "))
            digits_count = int(input("Enter digits count in password: "))
            special_characters_count = int(input("Enter special characters count in password: "))

            characters_count = alphabets_count + digits_count + special_characters_count

            ## check the total length with characters sum count
            ## print not valid if the sum is greater than length
            if characters_count > length:
                print("Characters total count is greater than the password length")
                startprogram()


            ## initializing the password
            password = []
            
            ## picking random alphabets
            for i in range(alphabets_count):
                password.append(random.choice(alphabets))


            ## picking random digits
            for i in range(digits_count):
                password.append(random.choice(digits))


            ## picking random alphabets
            for i in range(special_characters_count):
                password.append(random.choice(special_characters))


            ## if the total characters count is less than the password length
            ## add random characters to make it equal to the length
            if characters_count < length:
                random.shuffle(characters)
                for i in range(length - characters_count):
                    password.append(random.choice(characters))
            ## shuffling the resultant password
            random.shuffle(password)
            print("".join(password))
        except ValueError:
            print("Please enter enteger!")

startprogram()