legs=int(input("enter num of legs: "))
heads=int(input("enter num of heads: "))
flag=false
for cows in range(0,heads+1):
    hens=heads-cows
    cal_legs=cows*4 + hens*2
    if cal_legs==legs:
        flag=true
        break
if flag:
        print("cows: ",cows)
        print("hens: ",hens)
else:
        print("no solution")
