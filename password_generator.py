# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

lower   = "qwertyuiopasdfghjklzxcvbnm"
uppers  = "1234567890"
symbol  = "!@#$%^&*()"

all = lower + uppers + symbol
length = 16

password = "".join(random.sample(all,length))

print(password)