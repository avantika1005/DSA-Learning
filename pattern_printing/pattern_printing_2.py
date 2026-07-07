n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

a = ["A", "B", "C", "D", "E"]
for i in range(len(a)):
    for j in range(i + 1):
        print(a[i], end=" ")
    print()

a = ["A", "B", "C", "D", "E"]
for i in range(len(a)):
    for j in range(i, len(a)):
        print(a[j], end=" ")
    print()

a = ["A", "B", "C", "D", "E"]
for i in range(len(a) - 1, -1, -1):
    for j in range(i, len(a)):
        print(a[j], end=" ")
    print()
