#!/usr/bin/env python3

import math

print("Provide height:")
height = int(input())

print("Provide radius:")
radius = int(input())

print("Surface area of sphere:",
      2 * (math.pi * radius ** 2) + (2 * math.pi * radius * height))


