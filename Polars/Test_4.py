import polars as pl
import time

def complex_operation(row):
    result = sum([row[i] ** 2 for i in range(len(row))])
    return result

start_time = time.time()


df = pl.read_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/large_file.csv")

df= df.map_rows(complex_operation)

df.write_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/output2.csv")


end_time = time.time()

elapsed_time = end_time - start_time

print("Time taken to read, process, and write the CSV file: {:.2f} seconds".format(elapsed_time))
