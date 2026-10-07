# SOURCE DATA
data = [
    ['A', '20', '80'],
    ['B', '21', '90'],
    ['C', '22', '70']
]


# EXTRACT
print("Extracted Data:")
print(data)


# TRANSFORM
# Convert age and marks from string to integer
for row in data:
    row[1] = int(row[1])
    row[2] = int(row[2])


# Add grade
for row in data:

    if row[2] >= 80:
        row.append('A')

    elif row[2] >= 60:
        row.append('B')

    else:
        row.append('C')


# LOAD
database = []

for row in data:
    database.append(row)


print("\nLoaded Data:")

for row in database:
    print(row)
