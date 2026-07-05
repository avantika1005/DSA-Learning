#print 5 *  
n=5
print("*"*n)
#print 5 rows 5 col of *  i=rows and j=columns
n=5
for i in range(1,n+1):   # one row is geting linked to all columns and so on
    for j in range(1,n+1):  #i=1,j=(1,2,3,4,5) i=2,j=(1,2,3,4,5) i=3,j=(1,2,3,4,5) i=4,j=(1,2,3,4,5) i=5,j=(1,2,3,4,5)
        print("*",end="")
    print()                #time complexity is O(n^2) and space complexity is O(1)
#n=5 i need 1 *,2*,3*,4* 5*
n=5
for i in range(1,n+1):      #i=1,j=(1,1) i=2,j=(1,2) i=3,j=(1,2,3) i=4,j=(1,2,3,4) i=5,j=(1,2,3,4,5)
    for j in range(1,i+1):
        print("*",end="")
    print()                #time complexity is O(n^2) and space complexity is O(1)
