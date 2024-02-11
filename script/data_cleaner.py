import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('../data/data.csv')

# Display the first few rows before cleaning
print("Before Cleaning:")
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with a placeholder (e.g., for string columns)
df['string_column'] = df['string_column'].fillna('Unknown')

# Alternatively, drop rows with any missing values
# df = df.dropna()

# Convert data types
df['integer_column'] = pd.to_numeric(df['integer_column'], errors='coerce')  # Convert to numeric, coercing errors
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')  # Convert to datetime, coercing errors

# Rename columns for consistency
df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)

# Display the first few rows after cleaning
print("\nAfter Cleaning:")
print(df.head())

# Save the cleaned DataFrame back to a new CSV file
df.to_csv('../data/cleaned_data.csv', index=False)
