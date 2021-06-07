'''
    *
   *A*
  *A*A*
 *A*A*A*
*A*A*A*A*
'''
def printstring(string,times):
    for i in range(times):
        print(string,end='')

n=5
for i in range(0,n):
    printstring(" ",(n-i)-1)
    if i==0:
        print('*',end='')
    else:
        printstring('*A',i)
        print('*',end='')
    print()
