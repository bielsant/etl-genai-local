import logging

logging.basicConfig(level=logging.INFO)

def load_data(df, path: str):
    try:
        df.to_csv(path, index=False)
        logging.info(f"Dados salvos em {path}")
    except Exception as e:
        logging.error(f"Erro no load: {e}")