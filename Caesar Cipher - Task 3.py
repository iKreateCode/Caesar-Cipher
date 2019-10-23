import re
import math
#This is to import the required library so that it could function for this program 

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
            
def getKeyword():
    #This stores the 'Keyword' part of my code which is underneath 
    while True:
        Keyword = input("Enter your keyword: ")
        #This will ask the user enter their Keyword 
        if Keyword.isalpha() == True:
        #This will check if the user has entered atleast one letter
            return Keyword
        else:
            print("Keyword must only contain atleast one letter")
            #If they didnt enter atleast one letter then this will be printed out


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
                

def translatedMessage(Choice, Keyword, Message):
        letterCount = 0
        #This variable will store how many character there are in my message.
        newMessage = ""
        #This variable will store each character one by one from my message once its proccessed from the below code.
        Keyword = Keyword * math.ceil(len(Message)/len(Keyword))
        symbolcount = 0
        #This will store the amount of symbols in the message
        if Choice.lower() == "encrypt":
        #This shows that the underneath code is going to programmed for encrypt and will run the code if the selection equals to encrypt.
            while letterCount < len(Message):
                #This will check if there is any character counted and stored in the variable 'letterCount', and the length of the message.
                currentLetter = Message[letterCount]
                #This variable will store the current letter counted.
                isCurrentLetterALetter = bool(re.search("[a-zA-Z]",currentLetter))
                #This will check if the variable 'currentLetter' has letters stored or symbols, if it has symbol stored then it will ignore the bottom code and will go straight to .isAlpha().
                if isCurrentLetterALetter == True:
                #If the variable 'isCurrentLetterALetter' is a letter then it will carry on.
                    ASCIILetter = ord(currentLetter)
                    #Then it will convert the variable 'currentLetter' into an ASCII number and will be stored in the 'ASCIILetter' variable.
                
                    
                    if bool(re.search("[A-Z]", currentLetter)) == True:
                    #This will check through 'currentLetter' if it has capital letters through A-Z
                        keywordASCIIvalue = ord(Keyword[letterCount-symbolcount].upper())
                        #This will convert the keyword, the lettercount and symbolcount this will be done for uppercase also the letter count will minus symbolcount  
                        newASCIIvalue = ASCIILetter + keywordASCIIvalue - 64
                        #The ASCII value will store the code which will plus the ASCII letter with keywordASCIIvalue and then minus 64 because we are doing this for uppercase letter of ASCII value 
                    else:
                        keywordASCIIvalue = ord(Keyword[letterCount].lower())
                        #Else this part of the code will be done for the lower case letters
                        newASCIIvalue = ASCIILetter + keywordASCIIvalue - 96
                        #And this will plus the ASCII letter with the ASCII value of keyword then -96, this is going to be done for lower case letters for ASCII letter in encrypt as its different to upper case
                    newLetter = chr(newASCIIvalue)
                    #Then it will convert the ASCII value back into its letter and it will store it in the newLetter variable 
                                                                
                    if newLetter.isupper() == False and currentLetter.isupper() == True:
                    #This will check if the new converted letter is not upper and the original current letter is upper
                        newLetter = chr(newASCIIvalue - 26)
                        #Then this will -26 as theres 26 letters in the alphabet if we do not - 26 then it will show symbols or numbers
                    elif newLetter.islower() == False and currentLetter.islower() == True:
                    #This will check if the new converted letter is not lower and the original current letter is lower
                        newLetter = chr(newASCIIvalue - 26)
                        #Then this will -26 as theres 26 letters in the alphabet if we do not - 26 then it will show symbols or 

                    newMessage = newMessage + newLetter
                    #The newMessage variable will store the new encrypted letter and will add the proccessed letter to newMessage 
                else:
                    newMessage = newMessage + currentLetter
                    #This will add the non converted ASCII symbol directly to newMessage
                    symbolcount = symbolcount + 1
                    #This will add 1 each time there is a symbol to symbolcount, in the message

                letterCount = letterCount + 1
                #Finally it will accept when all the letters in the message has been proccessed and carry on to output the final message.

        else:
            while letterCount < len(Message):
            #This will check if there is any character counted and stored in the variable 'letterCount', and the length of the message.
                currentLetter = Message[letterCount]
                #This variable will store the current letter counted.
                isCurrentLetterALetter = bool(re.search("[a-zA-Z]",currentLetter))
                #This will check if the variable 'currentLetter' has letters stored or symbols, if it has symbol stored then it will ignore the bottom code and will go straight to .isAlpha().
                if isCurrentLetterALetter == True:
                #If the variable 'isCurrentLetterALetter' is a letter then it will carry on.
                    ASCIILetter = ord(currentLetter)
                    #Then it will convert the variable 'currentLetter' into an ASCII number and will be stored in the 'ASCIILetter' variable.
                    if bool(re.search("[A-Z]", currentLetter)) == True:
                    #This will check through 'currentLetter' if it has capital letters through A-Z
                        keywordASCIIvalue = ord(Keyword[letterCount-symbolcount].upper())
                        #This will convert the keyword, the lettercount and symbolcount this will be done for uppercase also the letter count will minus symbolcount
                        newASCIIvalue = ASCIILetter - keywordASCIIvalue + 64
                        #The ASCII value will store the code which will minus the ASCII letter with keywordASCIIvalue and then plus 64 because we are doing this for uppercase letter of ASCII value 
                    else:
                        keywordASCIIvalue = ord(Keyword[letterCount].lower())
                        #Else this part of the code will be done for the lower case letters
                        newASCIIvalue = ASCIILetter - keywordASCIIvalue + 96
                        #And this will minus the ASCII letter with the ASCII value of keyword then +96, this is going to be done for lower case letters in decrypt for ASCII letter as its different to upper case
                    newLetter = chr(newASCIIvalue)
                    #Then it will convert the ASCII value back into its letter and it will store it in the newLetter variable
                                                                
                    if newLetter.isupper() == False and currentLetter.isupper() == True:
                    #This will check if the new converted letter is not upper and the original current letter is upper
                        newLetter = chr(newASCIIvalue + 26)
                        #Then this will +26 as theres 26 letters in the alphabet if we do not +26 then it will show symbols or numbers
                    elif newLetter.islower() == False and currentLetter.islower() == True:
                    #This will check if the new converted letter is not lower and the original current letter is lower
                        newLetter = chr(newASCIIvalue + 26)
                        #Then this will +26 as theres 26 letters in the alphabet if we do not +26 then it will show symbols or numbers

                    newMessage = newMessage + newLetter
                    #The newMessage variable will store the new encrypted letter and will add the proccessed letter to newMessage
                else:
                    newMessage = newMessage + currentLetter
                    #This will add the non converted ASCII symbol directly to newMessage
                    symbolcount = symbolcount + 1
                    #This will add 1 each time there is a symbol to symbolcount, in the message

                letterCount = letterCount + 1
                #Finally it will accept when all the letters in the message has been proccessed and carry on to output the final message.

                
        return newMessage
        #Finally it will accept when all the letters in the message has been proccessed and carry on to output the finall message.
        
Choice = getSelection()
keyW1 = getKeyword()
print("Keyword accepted!")
keyW2 = getKeyword()
while keyW2 == keyW1:
    print("Keyword two cannot match keyword one")
    keyW2 = getKeyword()
print("Keyword accepted!")
Msg = getMessage()
translatedMSG = translatedMessage(Choice,keyW1,Msg)
secondtranslatedMSG = translatedMessage(Choice,keyW2,translatedMSG)
#This will proccess the second keyword and these are the variables that store the 'def' and other code
print("Output Result: " + secondtranslatedMSG)
#This will print out the proccessed message for encrypt or decrypt depending on the users choice

input()
