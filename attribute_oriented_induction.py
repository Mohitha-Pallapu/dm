data = [
    ['A', 'Bengaluru', 20],
    ['B', 'Bengaluru', 21],
    ['C', 'Mumbai', 22],
    ['D', 'Mumbai', 23],
    ['E', 'Delhi', 24]
]


# Generalize city into region
def generalize(city):

    if city == 'Bengaluru':
        return 'South'

    elif city == 'Mumbai':
        return 'West'

    else:
        return 'North'


groups = {}

for row in data:

    region = generalize(row[1])

    if region not in groups:
        groups[region] = 0

    groups[region] += 1


print("Generalized Data:")

for region, count in groups.items():
    print(region, ":", count)
