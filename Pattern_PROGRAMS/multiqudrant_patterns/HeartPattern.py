'''
  *****     *****
 *******   *******
********* *********
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
'''
def printString(string,times,step_value):
    for i in range(1,times,step_value):
        print(string,end="")
n=10#this is not rows.this is maximum number of stars
k=n//2 #integer division
#first half of heart pattern
for i in range(k,n+1,2):
    #logic for whitespace region-1
    printString(" ",n-i,2)
    #logic for star region-2
    printString("*",i+1,1)
    #logic for whitespace region-3
    printString(" ",(n-i)+1,1)
    #logic for star region-4
    printString("*",i+1,1)
    #new line
    print()
#second half of the heart pattern
for i in range(n,0,-1):
    for j in range(i,n):
        print(" ",end="")
    starNumber=(i*2)-1
    printString("*",(starNumber+1),1)
    print()
