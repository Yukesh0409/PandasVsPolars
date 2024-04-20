import pandas as pd
import time


def complex_operation(row):
    result = sum([row[col] ** 2 for col in row.index])
    return result


start_time = time.time()

df = pd.read_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/large_file.csv")
df['result'] = df.apply(complex_operation, axis=1)
df.to_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/output1.csv", index=False)

end_time = time.time()

elapsed_time = end_time - start_time

print("Time taken to read, process, and write the CSV file: {:.2f} seconds".format(elapsed_time))
