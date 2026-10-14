n = int(input("Enter the matrix size : "))

a = []

print("Enter the matrix elements:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

diagonal = 0
non_diagonal = 0

for i in range(n):
    for j in range(n):
        if i == j:
            diagonal = diagonal + a[i][j]
        else:
            non_diagonal = non_diagonal + a[i][j]

print("The sum of diagonal elements:", diagonal)
print("The sum of non-diagonal elements:", non_diagonal)