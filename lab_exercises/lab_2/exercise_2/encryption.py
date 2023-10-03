#!/usr/bin/env python3

print("Provide plaintext:")
plaintext = input()
cipherText = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextPosition = 0

while (plaintextPosition < len(plaintext)):

    ##  take a char from plain text
    plaintextChar = plaintext[plaintextPosition]

    ##  start from "A" in var `alphabet`
    alphabetPosition = 3

    ##  seek forwards until the plaintext char is found in `alphabet`
    while plaintextChar != alphabet[alphabetPosition]:
        alphabetPosition = alphabetPosition + 1

    ##  seek 3 steps backwards in `alphabet`
    alphabetPosition = alphabetPosition - 3

    ##  add this to ciphertext
    cipherText = cipherText + alphabet[alphabetPosition]

    ##  move onto next plaintext char
    plaintextPosition = plaintextPosition + 1

print(cipherText)
