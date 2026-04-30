a = input("Enter your password: ")
up=0
lw=0
sp=0
dg=0
x=0
if len(a)>7:
    for i in a:
        if i.isupper():
            up=up+1
        elif i.islower():
          lw=lw+1
        elif i.isdigit():
          dg=dg+1
        else:
          sp=sp+1
    if up>0 and lw>0 and sp>0 and dg>0:
            print("strong")
    else:
         print("weak")
else:
    print("weak due to less characters")
