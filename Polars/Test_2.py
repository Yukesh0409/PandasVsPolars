import polars as pl
import time

def complex_operation(row):
    result = sum([row[i] ** 2 for i in range(len(row))])
    return result

start_time = time.time() 
df = pl.read_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/large_file.csv")
end_time = time.time() 
read_elapsed_time = end_time - start_time

start_time = time.time()  
df1 = df.map_rows(complex_operation)
end_time = time.time()
transformation_elapsed_time = end_time - start_time

print("Time taken to read CSV file: {:.2f} seconds".format(read_elapsed_time))
print("Time taken to perform transformation: {:.2f} seconds".format(transformation_elapsed_time))
