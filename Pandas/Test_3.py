import pandas as pd
import time

def process_data(df):
    df['new_column'] = df['existing_column'] * 2
    return df

df = pd.read_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/large_file.csv")

start_time = time.time()
df.to_csv("/Users/cb-it-01-1088/Desktop/Projects/Projects/PandasVsPolars/modified_large_file1.csv", index=False)
end_time = time.time()

elapsed_time = end_time - start_time

print("Time taken to write the CSV file: {:.2f} seconds".format(elapsed_time))
