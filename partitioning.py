data = [
    [1, 'A', 80],
    [2, 'B', 90],
    [3, 'C', 70],
    [4, 'D', 85],
    [5, 'E', 95],
    [6, 'F', 75]
]


# 1. Horizontal Partitioning - split rows
print("Horizontal:")
print(data[:3])
print(data[3:])


# 2. Vertical Partitioning - split columns
print("\nVertical:")
print([[row[0], row[1]] for row in data])
print([[row[0], row[2]] for row in data])


# 3. Round Robin Partitioning - alternate rows
print("Round Robin:")

p1 = []
p2 = []

for i, row in enumerate(data):
    if i % 2 == 0:
        p1.append(row)
    else:
        p2.append(row)

print(p1)
print(p2)


# 4. Hash-based Partitioning
print("\nHash Based:")

p1 = []
p2 = []

for row in data:
    if row[0] % 2 == 0:
        p2.append(row)
    else:
        p1.append(row)

print(p1)
print(p2)
