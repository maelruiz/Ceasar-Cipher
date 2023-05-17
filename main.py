import string

filename = ""
letters = string.ascii_letters  # creates the letters variable using the ascii letters function
numbers = string.digits  # creates the numbers variable using ascii
characters = string.punctuation  # creates the punctuation variable


# Encrypts the character and tehn adds it to the word, by using the key - works with all characters
def encrypt(word, key):
    newWord = ""
    for character in word:
        #loop that iterates for every charachter in the loop and then encrypts it differently depending if the character is a letter, number, or punctuation.
        if character in letters:
            position = letters.find(character)
            newPosition = (position + key) % 52
            newCharacter = letters[newPosition]
        elif character in numbers:
            position = numbers.find(character)
            newPosition = (position + key) % 10
            newCharacter = numbers[newPosition]
        elif character in characters:
            position = characters.find(character)
            newPosition = (position + key) % 32
            newCharacter = characters[newPosition]
        else:
            newCharacter = character
        # adds the newcharacter to the newword
        newWord += newCharacter
    return newWord
# The same happens here, however, it does the opposite
def decrypt(word, key):
    newWord = ""
    for character in word:
        if character in letters:
            position = letters.find(character)
            newPosition = (position - key) % 52
            newCharacter = letters[newPosition]
        elif character in numbers:
            position = numbers.find(character)
            newPosition = (position - key) % 10
            newCharacter = numbers[newPosition]
        elif character in characters:
            position = characters.find(character)
            newPosition = (position - key) % 32
            newCharacter = characters[newPosition]
        else:
            newCharacter = character
        #adds the character to the newword
        newWord += newCharacter
    return str(newWord)

#gets the filename and the text and writes the text to the file
def writeto_file(filename, text):
    filename = txt(filename)
    with open(filename, 'w') as f:
        f.write(text)

#gets the filename and retrieves the text from the file 
def retrieve_file(filename):
    filename = txt(filename)
    with open(filename, 'r') as file:
        message = file.read().lower()
        return str(message), filename
        
#adds .txt to all filnames
def txt(filename):
    filename = filename + ".txt"
    return filename

while True:
    #asks the user for their choice
    choice = int(input("1 to encrypt \n2 to decrypt\n3 to exit\nEnter Choice: "))
    if choice == 1:
        #if the user chose 1 as their option - they will be asked what they want to encrypt, what the key should be and the filename. It is then encrypted and written to the file and printed to the console
        encryptWord = str(input("What word would you like to encrypt? "))
        encryptKey = int(input("What key would you like to use? "))
        filename = input("What file would you like to write to? ")
        newWord = encrypt(encryptWord, encryptKey)
        writeto_file(filename, newWord)
        print("This is the encrypted word: " + newWord)
            
    elif choice == 2:
        # if the user chooses '2', they will be asked for the filename of the file they want to read from (only works if the file is in the same directory). The program then asks for the key, and decryts the message, printing it and printing it to a file
        message, filename = retrieve_file(input("What file would you like to read from? "))
        encryptKey = int(input("What key would you like to use? "))
        newWord = decrypt(message, encryptKey)
        writeto_file(filename, newWord)
        print(newWord + " was successfully decrypted and has been printed to the file.")
        
        
    elif choice == 3:
        #this will stop the entre program and terminate the while True loop
        break  