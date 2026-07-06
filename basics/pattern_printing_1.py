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

#n=5 we need 1 in row 1, 2 2 in row 2, 3 3 3 in row 3, 4 4 4 4 in row 4, 5 5 5 5 5 in row 5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):  #i=1,j=(1,1) i=2,j=(1,2) i=3,j=(1,2,3) i=4,j=(1,2,3,4) i=5,j=(1,2,3,4,5)
        print(i,end="")
    print()                #time complexity is O(n^2) and space complexity is O(1)

#we need 1,1 2,2 3,3 4,4 5,5 in row 1,2,3,4,5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):  #i=1,j=(1,1) i=2,j=(1,2) i=3,j=(1,2,3) i=4,j=(1,2,3,4) i=5,j=(1,2,3,4,5)
        print(j,end="")
    print()                #time complexity is O(n^2) and space complexity is O(1)

#i need 1st row 5 stars 2nd row 4 and so on
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):  #i=1,j=(1,2,3,4,5) i=2,j=(1,2,3,4) i=3,j=(1,2,3) i=4,j=(1,2) i=5,j=(1)
        print("*",end="")
    print()                #time complexity is O(n^2) and space complexity is O(1)

#row 1=1 star,row 2=3 stars,row 3=5 stars,row 4=7 stars,row 5=9 stars
n=5
for i in range(1,n+1):      #we need to count space and stars in each
    for j in range(1,n-i+1):    # space i=1,j=(1) i=2,j=(1,2,3) i=3,j=(1,2,3,4,5) i=4,j=(1,2,3,4,5,6,7) i=5,j=(1,2,3,4,5,6,7,8,9 )
        print(" ",end=" ")
    for k in range(1,2*i): #star
        print("*",end=" ")
    print()                #time complexity is O(n^2) and space complexity is O(1)



n=5
for i in range(1,n+1):
    for j in range(1,i):
        print("",end=" ")
    for k in range(1,2*n-2*i+2):
        print("*",end=" ")
    print()                #time complexity is O(n^2) and space complexity is O(1)
         
