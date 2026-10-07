data = [
    ['2025', 'Laptop', 50000],
    ['2025', 'Phone', 30000],
    ['2026', 'Laptop', 60000],
    ['2026', 'Phone', 40000]
]


# Data Cube: Year -> Product -> Sales
cube = {}

for year, product, sales in data:

    if year not in cube:
        cube[year] = {}

    cube[year][product] = sales


print("Data Cube:")
print(cube)


# ROLL-UP: Total sales by year
print("\nRoll-up:")

for year in cube:
    print(year, sum(cube[year].values()))


# DRILL-DOWN: Show product-wise sales
print("\nDrill-down:")

for year in cube:
    for product in cube[year]:
        print(year, product, cube[year][product])


# SLICE: Select one year
print("\nSlice (2025):")
print(cube['2025'])


# DICE: Select years/products
print("\nDice:")

for year in ['2025', '2026']:
    print(year, cube[year]['Laptop'])
