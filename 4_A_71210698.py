A = int(input("Input: "))
print("Output :")
B = 2
for X in range(1,A+1):
    for Y in range(1,(2*A)):
        if X+Y==A+1 or Y-X==A-1:
            print("*",end="")
        elif X==A and Y!=B:
            print("*",end="")
            B=B+2
        else:
            print(end=" ")
    print()