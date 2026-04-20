from extract import extract_data
from transform import transform_data
from load import load_data

input_path = "data/input.csv"
output_path = "data/output.csv"

df = extract_data(input_path)

if df is not None:
    df = transform_data(df)
    load_data(df, output_path)

    print("\n[FINAL]")
    print(df)