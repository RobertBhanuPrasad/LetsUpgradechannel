# -*- coding: utf-8 -*-
"""Assignment-2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nJDlLI8z_3efD7jpONWvcnmkhViTWxfz
"""

num=int(input("enter the number"))
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

