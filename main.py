import csv
import random


# code for generating the csv files for read,transform and write operations
def generate_csv(rows, columns, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        header = [f'Column_{i}' for i in range(1, columns + 1)]
        writer.writerow(header)
        for _ in range(rows):
            row = [random.randint(0, 100) for _ in range(columns)]
            writer.writerow(row)

        print(f"CSV file with {rows} rows and {columns} columns generated successfully.")


generate_csv(1000, 100, '1000_rows_100_columns.csv')
generate_csv(100000, 1000, '100000_rows_1000_columns.csv')
# generate_csv(10000000, 10000, '10000000_rows_1000_columns.csv') #dont go for this unless your pc is a beast, instead use large_file.csv 
