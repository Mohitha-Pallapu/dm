# STAR SCHEMA
print("STAR SCHEMA")

product = {1: "Laptop", 2: "Phone"}
customer = {101: "A", 102: "B"}

sales = [
    [1, 101, 50000],
    [2, 102, 30000]
]

for p, c, amount in sales:
    print(product[p], customer[c], amount)


# SNOWFLAKE SCHEMA
print("\nSNOWFLAKE SCHEMA")

category = {1: "Electronics", 2: "Mobile"}

product = {
    101: ["Laptop", 1],
    102: ["Phone", 2]
}

for pid, info in product.items():
    print(info[0], category[info[1]])


# FACT CONSTELLATION
print("\nFACT CONSTELLATION")

sales = [
    [1, 101, 50000],
    [2, 102, 30000]
]

returns = [
    [1, 101, 2]
]

print("Sales:", sales)
print("Returns:", returns)
