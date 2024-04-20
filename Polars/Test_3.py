import polars as pl
import time


df = pl.read_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/large_file.csv")

start_time = time.time()
df.write_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/modified_large_file2.csv")
end_time = time.time()

elapsed_time = end_time - start_time

print("Time taken to write the CSV file: {:.2f} seconds".format(elapsed_time))
