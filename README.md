# Caesar Cipher

## Task 1 script
### About
A Caesar Cipher script written in Python, it involves Encryption and Decryption plus it’s all about Cryptography. 

It is a program that will ask the user to encrypt or decrypt and the user will input the choice of encrypting or decrypting, after that they will enter the message. Next, it will ask how many numbers do they want to shift the letters by, after the incrementation it will output the final message with the shifted letters. 

On the other hand if they have the choice of decrypting then they will input the encrypted message and the amount it has been shifted by, then it will output the original message before it was incremented.

### How does it work

The Caesar Cipher works by moving the original alphabet by a number amount of spaces for example “A” moved five places would be “F”/ “Apple” would be “Fuuqj” and you can call this encryption. This can be used to communicate to people without them knowing the original message. Decryption is when an Encrypted message is converted back to its original message for example “Fuuqj” would be “Apple”. This is the most effective way to send message which would be difficult for other people to decrypt.

### Example

```python
Enter your selection: Encrypt
Enter your message: i got a message
Enter your key: 4
Output result:  m ksx e qiwweki
```
```
Enter your selection: Decrypt
Enter your message: m ksx e qiwweki
Enter your key: 4
Output result:  i got a message
```

## Task 2 script
### About
Task 2 script will encrypt and decrypt a message by a keyword. The keyword will be repeated enough times until it matches the length of the message. The alphabet value of the message and keyword will be added to generate an encrypted message, or will be taken away to generate a decrypted message. There are 26 letters in the alphabet and if the final alphabet number is more than 26 then it will loop back to the start. 

### How does it work
For example if we use the keyword BENCH and message COMPUTINGRULES, the keyword BENCH will be repeated until it fits the 14 letter length message BENCHBENCHBENC, B represents the 2nd letter of the alphabet, E the 5th letter so on and so forth.

When both of the numbers from the keyword and message within the alphabet are added, the resultant number will represent the shifted letter from the alphabet.

### Example

```python
Enter your selection: Encrypt
Enter your keyword: Software
Enter your message: Python is great!
Output result: Inzblo nl mlbbl!
```
```
Enter your selection: Decrypt
Enter your keyword: Software
Enter your message: Inzblo nl mlbbl!
Output result: Python is great!
```
## Task 3 script
### About
In task 3 two keywords are needed to encrypt and decrypt a message. The first keyword will be repeated enough timed until it matches the length of the message, then each letter of the message will be encrypted or decrypted with the first keyword. Next, the second keyword will be repeated enough times again until it matches the length of the first encrypted/decrypted message and then the new letter of the new message will be encrypted or decrypted with the second keyword. 

### How does it work
For example if we use the first keyword as ADDER and message EXPANSIONCARDS, the keyword ADDER will be repeated until it fits the 14 letter length message ADDERADDERADDE, and then encrypted with the message which will be FBTFFTMSSUBVHY. It will be encrypted again but this time with the second keyword which is EXABYTEEXABYTE and the final encrypted message will be KYUHDNRXQVDTBC. 

### Example

```python
Enter your selection: Encrypt
Enter your keyword: Byte
Keyword accepted!
Enter your keyword: Funny
Keyword accepted!
Enter your message: This script is great, dont you think?
Output Result: Bbql xrkynt yf rorix, lhoy res txvgv?

```
```
Enter your selection: Decrypt
Enter your keyword: Byte
Keyword accepted!
Enter your keyword: Funny
Keyword accepted!
Enter your message: Bbql xrkynt yf rorix, lhoy res txvgv?
Output Result: This script is great, dont you think?
```
