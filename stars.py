s = int(input("Stars:"))
l = int(input("Lines:"))
b = int(input("Blocks:"))
for k in range(b):
    for i in range(l):
        for j in range(s):
            print("*",end=" ")
        print()
    l=l-1
    print("-------------------")
