import argparse
from extract import extract_data
from transform import transform_data
from load import load_data


def run_pipeline(input_path, output_path):
    df = extract_data(input_path)

    if df is not None:
        df = transform_data(df)
        load_data(df, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline ETL com Python")
    
    parser.add_argument("--input", required=True, help="Caminho do arquivo de entrada")
    parser.add_argument("--output", required=True, help="Caminho do arquivo de saída")

    args = parser.parse_args()

    run_pipeline(args.input, args.output)