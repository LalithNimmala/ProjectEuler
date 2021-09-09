def num_factors(x):
    Factors_of_x = []
    for i in range(2, x):
        if x % i == 0:
            Factors_of_x.append(i)
    if(len(Factors_of_x) == 0):
        return(0)
    else:
        print(Factors_of_x[-1])

def is_prime(x):
    if num_factors(x) == 0:
        print("is prime")

is_prime(6008)