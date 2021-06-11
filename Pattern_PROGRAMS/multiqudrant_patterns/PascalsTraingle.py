'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
rows=5 #rows_Number
coeff=1
for i in range(0,rows):
    for j in range(1,rows-i):
        print(" ",end="")
    for k in range(0,i+1):
        if k==0 or i==0:
            coeff=1
        else:
            coeff=coeff*(i-k+1)//k

        print(coeff,end=" ")
    print()
