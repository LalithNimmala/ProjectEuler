T = []
P = []
H = []

for i in range(1, 100000):
    T.append(int(i*(i+1)/2))
    P.append(int(i*((3*i)-1)/2))
    H.append(int(i*((2*i)-1)))

for x in T:
    if x in P and x in H:
        print(x)