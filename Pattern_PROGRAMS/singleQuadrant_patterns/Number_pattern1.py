#One Quadrant problem
'''
5 5 5 5 5  0-whitespaces
  4 4 4 4  2-whitespaces
    3 3 3  4-whitespaces
      2 2  6-whitespaces
        1  8-whitespaces
'''#n=5
#this function is a reusable code
def printString(string,times):
    for i in range(times):
        print(string,end="")
n=5#total no. of rows
for i in range(0,n):
    #we have leading whitespaces
    #write logic for the same
    printString(" ",i*2)

    #element-* pattern
    printString(str(n-i)+' ',n-i)#calling function
    #adding a new line
    print()#(OR) u can use print("\r")
