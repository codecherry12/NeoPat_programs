'''
0 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
0 1 1 1 0
'''
rows=5
columns=5
for i in range(1,rows+1):
    for j in range(1,columns+1):
        #print corner elements
        if ((i==1 or i==rows) and (j==1 or j==columns)):
            print("0 ",end="")
        elif ((i==1 or i==rows) or (j==1 or j==columns)):
            #print edge elements
            print("1 ",end="")
        else:
            #print center elements
            print("0 ",end="")
    print()
