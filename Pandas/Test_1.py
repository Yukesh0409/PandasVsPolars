import pandas as pd
import time

start_time = time.time()

df = pd.read_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/large_file.csv")

end_time = time.time() 

elapsed_time = end_time - start_time
print("Time taken to read and print DataFrame: {:.2f} seconds".format(elapsed_time))
