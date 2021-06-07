#One Quadrant problem
'''
* * * * *
* * * *
* * *
* *
*
'''#n=5
#this function is a reusable code
def printString(string,times):
    for i in range(times):
        print(string,end="")
n=5#total no. of rows
for i in range(0,n):
    #element-* pattern
    printString("* ",n-i)#calling function for printing the string
    #we have leading whitespaces
    #write logic for the same
    #printString(" ",i*2)#calling for printing the whitespaces

    #adding a new line
    print()#(OR) u can use print("\r")
