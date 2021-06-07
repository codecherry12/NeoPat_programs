#One Quadrant problem
'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''#n=5
#this function is a reusable code
def printString(string,times):
    for i in range(times):
        print(string,end="")
n=5#total no. of rows
for i in range(1,n+1):
    #we have leading whitespaces
    #write logic for the same
    printString(" ",(n-i))#calling for printing the whitespaces


    #element-pattern
    for j in range(1,i+1):
        print(j,end=' ')
    #adding a new line
    print()#(OR) u can use print("\r")
