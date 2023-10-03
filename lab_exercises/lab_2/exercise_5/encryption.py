#!/usr/bin/env python3

plain_t = input()

cipher_t = ""

plain_t_pos = 0


while plain_t_pos < len(plain_t):

    plain_t_char = plain_t[plain_t_pos]

    ascii_value = ord(plain_t_char)

    ascii_value = ascii_value - 3

    cipher_t = cipher_t + chr(ascii_value)

    plain_t_pos = plain_t_pos + 1

    
print(cipher_t)
