#Insert an element in the array 

n = int(input("Enter array size: "))

arr = [0] * (n + 1)

for i in range(n):
    arr[i] = int(input("Enter element: "))

print("Original array:", arr[:n])

element = int(input("Enter element to insert : "))
position = int(input("Enter position : "))

if position < 0 or position > n:
    print("Invalid position")
else:
    i = n
    while i > position:
        arr[i] = arr[i - 1]
        i = i - 1

    arr[position] = element
    n = n + 1

    print("Array after insertion:", arr[:n])


# Deletion of element in array

n = int(input("Enter array size: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

print("Original array:", arr)

pos = int(input("Enter position to delete : "))

if pos < 0 or pos >= n:
    print("Invalid position")
else:
    i = pos

    while i < n - 1:
        arr[i] = arr[i + 1]
        i = i + 1

    n = n - 1

    print("Array after deletion:", arr[:n])



# Product of two matrix

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

a = []
b = []
result = []

print("Enter first matrix: ")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    a.append(row)

print("Enter second matrix: ")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    b.append(row)

for i in range(r):
    row = []
    for j in range(c):
        sum = 0
        for k in range(c):
            sum = sum + a[i][k] * b[k][j]
        row.append(sum)
    result.append(row)

print("Product of matrices : ")
for row in result:
    print(row)




#Sum of diagnol and non diagnol elements of matrix 

n = int(input("Enter matrix size : "))

a = []

print("Enter matrix elements : ")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

diagonal = 0
non_diagonal = 0

for i in range(n):
    for j in range(n):
        if (i == j):
            diagonal = diagonal + a[i][j]
        else:
            non_diagonal = non_diagonal + a[i][j]

print("Sum of diagonal elements:", diagonal)
print("Sum of non-diagonal elements:", non_diagonal)








