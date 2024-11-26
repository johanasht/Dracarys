import pandas as pd

df = pd.read_csv('gofood_dataset.csv')

unique_values = df.head(100)['display'].unique()

# Enclose each unique value within apostrophes
unique_values_with_apostrophes = ["'" + str(value) + "'" for value in unique_values]

# Join unique values into a single string separated by whitespace
unique_values_str = ' '.join(unique_values_with_apostrophes)
num_unique_values = len(unique_values)

print("Num of unique:", num_unique_values)
print("Unique:", unique_values_str)