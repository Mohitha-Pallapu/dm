from collections import Counter

transactions = [
    ['A','B','C'],
    ['A','B'],
    ['A','C'],
    ['A','B','C'],
    ['B','C']
]

min_support = 2

# Count item frequencies
count = Counter()

for t in transactions:
    for item in t:
        count[item] += 1

# Keep frequent items
frequent = {item:n for item,n in count.items()
            if n >= min_support}

print("Frequent Items:")
print(frequent)

# FP-Tree
tree = {}

for t in transactions:
    p = tree

    for x in t:
        if x not in p:
            p[x] = [0, {}]

        p[x][0] += 1
        p = p[x][1]

# Print FP-Tree
print("\nFP-Tree:")

def show(t, s=""):
    for x in t:
        print(s + x, ":", t[x][0])
        show(t[x][1], s + "  ")

show(tree)
