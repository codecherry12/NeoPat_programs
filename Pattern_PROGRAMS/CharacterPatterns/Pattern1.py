"""
A A A A A
A A A B B
A A C C C
A D D D D
E E E E E """

n=5
ch='A'
for i in range(0,n):
    count=(n-1)-i
    for j in range(1,count+1):
        print("A ",end="")
    for k in range(0,i+1):
        print(ch,end=" ")
    print()
    x=ord(ch)+1
    ch=chr(x)
