A = input("Input : ")
B = len(A)
print("Output :",end="")

for C in range(B):
    print(A[:C])
for D in range(B,0,-1):
    print(A[:D])