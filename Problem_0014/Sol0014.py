max_len = 0

def gen_dict(x):
    y = []
    while x != 1:
        if x%2 == 0:
            x = int(x/2)
        else:
            x = (3*x) + 1
        y.append(x)
    return(y)


for i in reversed(range(1,1000000)):
    if len(gen_dict(i)) > max_len:
        max_len = len(gen_dict(i))
        x = i
        y = gen_dict(i)

print(x, y)