"""
      A
    A B A
  A B C B A
A B C D C B A
"""
def printstring(string,times):
    for i in range(times):
        print(string,end='')
n=4
for i in range(1,n+1):
    printstring(' ',(n-i)*2)
    for j in range(0,i):
        print(chr(65+j),end=" ")
    x=65+(i-1)
    while x>=66:
        print(chr(x-1),end=' ')
        x-=1
    print()
