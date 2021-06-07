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
    #we have leading whitespaces
    #write logic for the same
    printString(" ",(n-i))#calling for printing the whitespaces


    #element-* pattern
    printString(" *",i)#calling function for printing the string
    #adding a new line
    print()#(OR) u can use print("\r")
