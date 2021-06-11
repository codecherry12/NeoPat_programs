'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

rows=5
#first half of the patter
i=rows
while i>=1:
    j=i
    while j>=1:
        print(j,end=" ")
        j-=1
    i-=1
    print()
#second half
for i in range(2,rows+1):
    j=i
    while j>=1:
        print(j,end=" ")
        j-=1
    print()
