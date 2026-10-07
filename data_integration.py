import pandas as pd

data1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['A', 'B', 'C']
})

data2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Marks': [80, 90, 85]
})

# Integrate using common ID
result = pd.merge(data1, data2, on='ID')

print(result)
