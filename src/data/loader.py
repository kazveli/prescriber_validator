import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath, skiprows=0):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"[Dataldoader] Arquivo não encontrado: {filepath}")
        self.filepath = filepath
        self.skiprows = skiprows

    def load(self):
        df = pd.read_excel(self.filepath, skiprows=self.skiprows)
        df.columns = df.columns.str.strip()
        return df
    
    def export(self, df, output_path):
        df.to_excel(output_path, index=False)