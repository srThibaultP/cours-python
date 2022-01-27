a,b=0,10
while a<b:
    print(a, end="|")
    a+=1
print("\n")
while b>0:
    b -= 1
    if b%2 != 0:
        print(b, end="|")