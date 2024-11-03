#Plan (Make a Code Generator (Encoding & Decoding for the following Ciphers
#1. Ceaser
#2. Baconian
#2. Nihilist))

import random
import numpy as np
import time

#1. Ceaser Cipher
#___________________________________________
def ceaserCipher():
    text = ""
    if mode == "E":
        plaintext = input("Input Plaintext Message: ")
        ceaserKey = int(input("Choose a Key: "))
        for char in plaintext:
            if char.isalpha():
                start = ord("A") if char.isupper() else ord("a")
                encryptedChar = chr((ord(char) - start + ceaserKey) % 26 + start)
                text += encryptedChar
            else:
                text += char
        print("Encrypted Message " + text)
    
    if mode == "D":
        ciphertext = input("Input Ciphertext Message: ")
        ceaserKey = int(input("What is the Key?: "))
        for char in ciphertext:
            if char.isalpha():
                start = ord("A") if char.isupper() else ord("a")
                decryptedChar = chr((ord(char) - start - ceaserKey) % 26 + start)
                text += decryptedChar
            else:
                text += char
        print("Decrypted Message " + text)

#____________________________________________________________________________________________
#2. Baconian Cipher
def baconianCipher():
    ciphertext = " "
    baconianDictionary = {
        'a': "AAAAA", 'b' : "AAAAB", 'c' : "AAABA", 'd' : "AAABB", 'e' : "AABAA",
        'f' : "AABAB", 'g' : "AABBA", 'h' : "AABBB", 'i' : "ABAAA", 'j' : "ABAAA",
        'k' : "ABAAB", 'l' : "ABABA", 'm' : "ABABB", 'n' : "ABBAA", 'o' : "ABBAB",
        'p' : "ABBBA", 'q' : "ABBBB", 'r' : "BAAAA", 's' : "BAAAB", 't' : "BAABA",
        'u' : "BAABB", 'v': "BAABB", 'w': "BABAA", 'x' : "BABAB", 'y' : "BABBA", 
        'z': "BABBB"
    }
    decryption_table = {value: key for key, value in baconianDictionary.items()}
    if mode == "E":
        plaintext = input("Input Plaintext Message: ")
        text = plaintext.replace(" ", "")
        for char in text.lower():
            if char in baconianDictionary:
                ciphertext += baconianDictionary[char]
        print("Encrypted Message: " + ciphertext)
    if mode == "D":
        ciphertext = input("Input Ciphertext Message (No Spaces): ")
        baconianSegments = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
        plaintext = []
        for segment in baconianSegments:
            letter = decryption_table.get(segment, "?")
            plaintext.append(letter)
        print("Decrypted Message: " + "".join(plaintext))
        
#____________________________________________________________________________________________
#3. Nihilist Cipher

def polybius_square():
    polybiusKey = input("Please Input a Polybius Key: ")
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    polybiusKey = polybiusKey.lower().replace("j", "k")
    polybiusChars = ""
    for char in polybiusKey:
        if char not in polybiusChars:
            polybiusChars += char
    remainingChars = "".join(i for i in alphabet if i not in polybiusChars)
    polybiusChars = polybiusChars + remainingChars 
    return np.array(list(polybiusChars)).reshape(5,5)

def nihilistCipher():
    polybiusSquare = polybius_square()
    print(polybiusSquare)
    referenceTerm = input("Please Input a Reference Term: ")
    referenceTerm = referenceTerm.lower().replace("i", "j")
    referenceKey = []
    for char in referenceTerm:
        if char in polybiusSquare:
            row, col = np.where(polybiusSquare == char)
            referenceKey.append(str(row[0] + 1) + str(col[0] + 1))
            i=0
    if mode == "E":
        plaintext = input("Plaintext: ")
        plaintext = plaintext.lower().replace("i", "j")
        ciphertext = []
        print("Polybius Square")
        print(polybiusSquare)
        for char in plaintext:
            if char in polybiusSquare:
                row, col = np.where(polybiusSquare == char)
                ciphertext.append(str(int(str(row[0] + 1) + str(col[0] + 1)) + int(referenceKey[i])))
                i += 1
                if i == len(referenceKey):
                    i = 0
        print("Encrypted Message: " + " ".join(ciphertext))
    
    if mode == "D":
        ciphertext = input("Ciphertext (as a sequence of #s with spaces): ")
        ciphertext_nums = ciphertext.split()

        plaintext = []
        for num in range(len(ciphertext_nums)):
            ciphertext_nums[num] = str(int(ciphertext_nums[num]) - int(referenceKey[i]))
            i += 1
            if i == len(referenceKey):
                i = 0
        for num in ciphertext_nums:
            row = int(num[0]) - 1
            col = int(num[1]) - 1

            plaintext.append(polybiusSquare[row][col])
        print("Decrypted Message: " + "".join(plaintext))


cont = 0
ciphertext = ""

while cont == 0:
    print("""Please Choose a Cipher (Input #)
#1 Ceaser Cipher
#2 Baconian Cipher
#3 Nihilist Cipher """)
    choice = int(input())
    mode = input("Encryption (E) or Decryption (D): ")
    mode = mode.upper()
    if choice == 1:
        ceaserCipher()
        time.sleep(3)
        print()
    if choice == 2:
        baconianCipher()
        time.sleep(3)
        print()
    if choice == 3:
        nihilistCipher()
        time.sleep(3)
        print()
    cont = int(input("Press 0 to Continue: "))