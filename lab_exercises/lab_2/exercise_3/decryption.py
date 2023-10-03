#!/usr/bin/env python3

##  $ python3 -m unittest

def decryption(cipherText):

    plainText = ""
    alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
    ciphertextPosition = 0

    while (ciphertextPosition < len(cipherText)):

        ##  take a char from ciphertext
        ciphertextChar = cipherText[ciphertextPosition]

        ##  start from "A" in var `alphabet`
        alphabetPosition = 3

        ##  seek forwards until the ciphertext char is found in `alphabet`
        while ciphertextChar != alphabet[alphabetPosition]:
            alphabetPosition = alphabetPosition + 1

        ##  seek 3 steps forward in `alphabet`
        alphabetPosition = alphabetPosition + 3

        ##  store this char in plaintext
        plainText = plainText + alphabet[alphabetPosition]

        ##  move onto next ciphertext char
        ciphertextPosition = ciphertextPosition + 1

    print(cipherText, "=>", plainText)
    return plainText

if __name__ == '__main__':
    
    print("Provide ciphertext")
    cipherText = input()
    decryption(cipherText)

