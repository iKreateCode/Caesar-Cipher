import re

def getSelection():
    #This code defines and stores the code i have written underneath and this stores the code for selection.
    while True:
        selection = input("Enter your selection: ").lower()
        if selection == ("encrypt") or selection == ("decrypt"):
            return selection
        #This code will ask the user to enter their selection and will check if they wrote encrypt or decrypt if they have then it will accept it.
        else:
            print("Enter either Encrypt or Decrypt")
            #If the user hasnt entered the required selection then this part will be printed out

def getMessage():
    while True:
            message = input("Enter your message: ")
            #This will ask the user to enter their message
            if bool(re.search("[a-zA-Z]",message)) == True:
            #This will search through the message to see if their is atleast one character
                return message
            #Then the next code will check through their message and will accept their message if they have typed in atleast one character.
            else:
                print("Enter atleast one character")
                #If they havnt wrote atleast one letter then this will be printed out
                
def getKey():
    #This stores the 'Key' part of my code which is underneath 
    while True:
        key = input("Enter your key: ")
        #This will ask the user enter their positive key
        try:
            key = int(key)
            #This code will check if the entered character is an integer
            if key >= 1 and key <= 26:
                return key
            #Next it will check if the character is more than or equal to 1 and less than or equal to 26.
        except ValueError:
            print("Enter atleast one positive integer")
            #This last section will be printed out if the character is not the required character.

def translatedMessage():
    while True:
        if Choice.lower() == "encrypt":
            #This shows that the underneath code is going to programmed for encrypt and will run the code if the selection equals to encrypt.
            letterCount = 0
            #This variable will store how many character there are in my message.           
            newMessage = " "
            #This variable will store each character one by one from my message once its proccessed from the below code. 
            

            while letterCount < len(Msg):
                #This will check if there is any character counted and stored in the variable 'letterCount', and the length of the message.
                currentLetter = Msg[letterCount]
                #This variable will store the current letter counted.
                isCurrentLetterALetter = bool(re.search("[a-zA-Z]",currentLetter))
                #This will check if the variable 'currentLetter' has letters stored or symbols, if it has symbol stored then it will ignore the bottom code and will go straight to .isAlpha().
                if isCurrentLetterALetter == True:
                    #If the variable 'isCurrentLetterALetter' a letter then it will carry on.
                    ASCIILetter = ord(currentLetter)
                    #Then it will convert the variable 'currentLetter' into an ASCII number and will be stored in the 'ASCIILetter' variable.
                    newASCII = ASCIILetter + shift
                    #After its converted into an ASCII number it will add the key number to the 'ASCIILetter' and stored in 'newASCII'.
                    newLetter = chr(newASCII)
                    #Then it will convert the new ASCII number back into its new letter and will stored in 'newLetter' variable. 
                                                                
                    if newLetter.isalpha() == False:
                        #This will check the letter if its a symbol or a letter.
                        newLetter = chr(newASCII - 26)
                        #If its not a letter (False) then it will -26 making it go back to the start of the alphabet.

                    newMessage = newMessage + newLetter
                    #Then it will add the new character to the variable 'newMessage' at the top.
                else:
                    newMessage = newMessage + currentLetter
                    #if its a symbol then it will be added to the variable 'newMessage'

                letterCount = letterCount + 1
                #Then it will add the amount of characters there are in the message one by one making sure it has gone through all the letters in the message

                
            return newMessage
                    #Finally it will accept when all the letters in the message has been proccessed and carry on to output the finall message.

        else:
            if Choice.lower() == "decrypt":
                letterCount = 0
                newMessage = " "
                
            while letterCount < len(Msg):
            #This will check if there is any character counted and stored in the variable 'letterCount', and the length of the message.
                currentLetter = Msg[letterCount]
                #This variable will store the current letter counted.
                isCurrentLetterALetter = bool(re.search("[a-zA-Z]",currentLetter))
                #This will check if the variable 'currentLetter' has letters stored or symbols, if it has symbol stored then it will ignore the bottom code and will go straight to .isAlpha().
                if isCurrentLetterALetter == True:
                    #If the variable 'isCurrentLetterALetter' a letter then it will carry on.
                    ASCIILetter = ord(currentLetter)
                    #Then it will convert the variable 'currentLetter' into an ASCII number and will be stored in the 'ASCIILetter' variable.
                    newASCII = ASCIILetter - shift
                    #After its converted into an ASCII number it will minus the key number to the 'ASCIILetter' and stored in 'newASCII'.
                    newLetter = chr(newASCII)
                    #Then it will convert the new ASCII number back into its new letter and will stored in 'newLetter' variable. 
                                                                
                    if newLetter.isalpha() == False:
                        #This will check the letter if its a symbol or a letter.
                        newLetter = chr(newASCII + 26)
                        #If its not a letter (False) then it will +26 making it go forward to the start of the alphabet.

                    newMessage = newMessage + newLetter
                    #Then it will add the new character to the variable 'newMessage' at the top.
                else:
                    newMessage = newMessage + currentLetter
                    #if its a symbol then it will be added to the variable 'newMessage'

                letterCount = letterCount + 1
                #Then it will add the amount of characters there are in the message one by one making sure it has gone through all the letters in the message

                   
        
        return newMessage
        #Finally it will accept when all the letters in the message has been proccessed and carry on to output the finall message.

Choice = getSelection()
Msg = getMessage()
shift = getKey()
translatedMSG = translatedMessage()
#These variables will store the 'def' variables so it could be printed out when referred.
print("Output result: " + translatedMSG)
#This will print out the proccessed message once its finished.


input()
