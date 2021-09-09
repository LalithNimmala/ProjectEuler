def sum_multiple():
    total = 0
    for i in range(3,1001):
        if (i % 3 == 0) or (i % 5 == 0):
            total = total + i
    return(total)


print(sum_multiple())