"""
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
Answer = 1366
"""

x = str(2**1000)
y = 0

for each in (list(x)):
    y = y + int(each)

print(y)