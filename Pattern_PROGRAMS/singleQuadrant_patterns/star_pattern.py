#One Quadrant problem
'''
*
* *
* * *
* * * *
* * * * *
'''#n=5
#this function is a reusable code
def printString(string,times):
    for i in range(times):
        print(string,end="")
n=5#total no. of rows
for i in range(1,n+1):
    #no leading whitespaces
    #write logic for the same

    #element-* pattern
    printString("* ",i)#calling function
    #adding a new line
    print()#(OR) u can use print("\r")
