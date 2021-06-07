#One Quadrant problem
'''
* * * * *  0-whitespaces
  * * * *  2-whitespaces
    * * *  4-whitespaces
      * *  6-whitespaces
        *  8-whitespaces
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
    printString("* ",n-i)#calling function
    #adding a new line
    print()#(OR) u can use print("\r")
