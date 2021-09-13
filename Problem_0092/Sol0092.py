num_of_89s = 0


def squ_the_digits(x):
    y = str(x)
    sum = 0
    for digit in y:
        sum = sum + (int(digit)*int(digit))
    return(sum)

for i in range(1, 1000001):
    if squ_the_digits(i) == 89:
        num_of_89s = num_of_89s + 1
    else:
        squ_the_digits(sum)