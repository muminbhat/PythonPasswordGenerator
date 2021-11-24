import random

small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "12345678901234567890"
special = "*****&&&&&^^^^^$$$$$#####*@&$*#@#$%"

all = (small + capital + numbers + special)
len = 16

Password = "".join(random.sample(all, len))

print("New unbreakble key generated:", Password )