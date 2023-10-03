#!/usr/bin/env python3

cipher_t = input()

plain_t = ""

cipher_t_pos = 0


while cipher_t_pos < len(cipher_t):

    cipher_t_char = cipher_t[cipher_t_pos]

    ascii_value = ord(cipher_t_char)

    ascii_value = ascii_value + 3

    plain_t = plain_t + chr(ascii_value)

    cipher_t_pos = cipher_t_pos + 1

    
print(plain_t)
