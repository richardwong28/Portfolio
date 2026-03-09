import pandas as pd
import os

def clean_and_save(data, filename):
    if not data:
        raise ValueError("Data kosong! Scraper tidak mendapatkan hasil apapun.")
    
    df = pd.DataFrame(data)

    if 'harga_raw' not in df.columns:
        raise KeyError(f"Kolom 'harga_raw' tidak ditemukan. Kolom tersedia: {df.columns.tolist()}")
    
    df['harga_angka'] = df['harga_raw'].str.replace(r'£', '', regex=True).replace('', '0').fillna('0').astype(float)
    
    df.drop_duplicates(subset=['nama'], inplace=True)

    if not os.path.exists('output'):
        os.makedirs('output')

    output_path = f"output/{filename}.xlsx"
    df.to_excel(output_path, index=False)
    return output_path