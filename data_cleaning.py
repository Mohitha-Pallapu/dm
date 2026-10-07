import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'B'],
    'Age': [20, None, 22, None],
    'Marks': [80, 90, None, 90]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)
