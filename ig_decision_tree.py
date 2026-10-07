import math

# Dataset: [Outlook, Play]
data = [
    ['Sunny', 'No'],
    ['Sunny', 'No'],
    ['Overcast', 'Yes'],
    ['Rain', 'Yes'],
    ['Rain', 'Yes'],
    ['Rain', 'No']
]


# Function to calculate entropy
def calculate_entropy(data):
    yes = 0
    no = 0

    for row in data:
        if row[1] == 'Yes':
            yes += 1
        else:
            no += 1

    total = len(data)
    entropy = 0

    if yes > 0:
        p_yes = yes / total
        entropy -= p_yes * math.log2(p_yes)

    if no > 0:
        p_no = no / total
        entropy -= p_no * math.log2(p_no)

    return entropy


# Calculate entropy of the complete dataset
total_entropy = calculate_entropy(data)


# Find different values of Outlook
outlook_values = set(x[0] for x in data)


# Calculate weighted entropy after splitting on Outlook
weighted_entropy = 0

for value in outlook_values:

    subset = []

    for row in data:
        if row[0] == value:
            subset.append(row)

    weight = len(subset) / len(data)
    weighted_entropy += weight * calculate_entropy(subset)


# Information Gain
information_gain = total_entropy - weighted_entropy


print("Entropy =", total_entropy)
print("Information Gain =", round(information_gain,3))

print("\nDecision Tree")
print("       Outlook")

for value in outlook_values:

    # Create a subset for the current Outlook value
    subset = []

    for row in data:
        if row[0] == value:
            subset.append(row)

    # Check the result for this subset
    yes_count = 0
    no_count = 0

    for row in subset:
        if row[1] == 'Yes':
            yes_count += 1
        else:
            no_count += 1

    if yes_count == len(subset):
        result = "Yes"

    elif no_count == len(subset):
        result = "No"

    else:
        result = "Mixed"

    print("       |--", value, "-->", result)
