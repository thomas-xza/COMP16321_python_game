#!/usr/bin/env python3

def read_file():

    file_as_array = []

    with open('input.txt', encoding="utf-8") as f:

        for line in f:

            file_as_array.append(line.strip())


    return file_as_array
