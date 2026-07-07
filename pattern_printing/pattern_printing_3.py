a=[1,2,3,4,5]
n=5
for i in range(n+1):
    print()
    for j in range(1,i+1):
        print(a[i-1],end=" ")
print()

n = 5
for i in range(1, n + 1):
    print()
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
print()

n=5
for i in range(1,n+1):
    print()
    for j in range(i):
        print(j%2,end=" ")
print()
