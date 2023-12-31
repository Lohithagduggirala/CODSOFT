# -*- coding: utf-8 -*-
"""Password Generator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c-K9eCXECZ4gdJhNt1c4WwVUzuz_N3wj
"""

import random
length = int(input("Enter the length of the password : "))
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','*','(',')','?','[',']','_']
no_letters = int(input("How many letters do you wish to have in your password?\n"))
no_digits = int(input("How many digits do you wish to have in your password?\n"))
no_symbols = int(input("How many symbols do you wish to have in your password?\n"))
if length == (no_letters+no_digits+no_symbols):
    password_list = []
    for i in range (1,no_letters+1):
      char = random.choice(letters)
      password_list += char
    for i in range(1,no_digits+1):
      digit = random.choice(digits)
      password_list += digit
    for i in range(1,no_symbols+1):
      char = random.choice(symbols)
      password_list += char
    random.shuffle(password_list)
    password = ""
    for i in password_list:
      password += i
    print("Your password is :",password)
else:
    print("Length of password is not equal to the given length of characters.")