import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def extract_data(path: str):
    try:
        df = pd.read_csv(path)
        logging.info(f"{len(df)} registros carregados")
        return df
    except Exception as e:
        logging.error(f"Erro na extração: {e}")
        return None