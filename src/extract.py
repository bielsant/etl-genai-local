import pandas as pd

def extract_data(path: str):
    try:
        df = pd.read_csv(path)
        print(f"[EXTRACT] {len(df)} registros carregados")
        return df
    except Exception as e:
        print(f"[ERRO - EXTRACT] {e}")
        return None