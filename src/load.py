def load_data(df, path: str):
    try:
        df.to_csv(path, index=False)
        print(f"[LOAD] Dados salvos em: {path}")
    except Exception as e:
        print(f"[ERRO - LOAD] {e}")