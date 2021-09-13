def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return(False)
    return(True)

for i in range(1, 100):
    if is_prime(i):
        print(i)

def is_pandigital(x):
    x_len = len(x)
    for i in range(1, x_len+1):
        if i in str(x):
            