import pandas as pd
import time

def complex_operation(row):
    result = sum([row[col] ** 2 for col in row.index])
    return result

start_time = time.time()
df = pd.read_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/large_file.csv")
end_time = time.time() 
read_elapsed_time = end_time - start_time


start_time = time.time()  
df['result'] = df.apply(complex_operation, axis=1)
end_time = time.time()
transformation_elapsed_time = end_time - start_time

print("Time taken to read CSV file: {:.2f} seconds".format(read_elapsed_time))
print("Time taken to perform transformation: {:.2f} seconds".format(transformation_elapsed_time))
