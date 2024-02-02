import pandas as pd

# Read the CSV file into a pandas DataFrame
csv_file_path = 'data1.csv'
df = pd.read_csv(csv_file_path)

# Save the DataFrame to an Excel file
excel_file_path = 'data1.xlsx'
df.to_excel(excel_file_path, index=False)

# Read the CSV file into a pandas DataFrame
csv_file_path = 'data2.csv'
df = pd.read_csv(csv_file_path)

# Save the DataFrame to an Excel file
excel_file_path = 'data2.xlsx'
df.to_excel(excel_file_path, index=False)

# Read the first Excel sheet
df1 = pd.read_excel('data1.xlsx')

# Read the second Excel sheet
df2 = pd.read_excel('data2.xlsx')

# # Merge the two dataframes based on the 'Rating' column
# merged_df = pd.merge(df1, df2, on='Ratings', how='inner')

# # Save the merged data to a new Excel sheet
# merged_df.to_excel('compared_data.xlsx', index=False)

# Merge the two dataframes on the 'Title' column
merged_df = pd.merge(df1, df2, on='Title', suffixes=('Sheet1', 'Sheet2'))
print(merged_df.columns)

# For each row, select the highest rating between the two sheets
merged_df['Highest_Rating'] = merged_df[['RatingsSheet1', 'RatingsSheet2']].max(axis=1)

# Select only the columns you want to keep in the new sheet
result_df = merged_df[['Title', 'Highest_Rating', 'PriceSheet1', 'PriceSheet2']]

# Save the compared data to a new Excel sheet
result_df.to_excel("compared_data.xlsx", index=False)

