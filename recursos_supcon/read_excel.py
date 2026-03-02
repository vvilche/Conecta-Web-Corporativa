import pandas as pd

file_path = "SUPCON Oversea Product List (1).xlsx"
try:
    xl = pd.ExcelFile(file_path)
    print("Sheets available:", xl.sheet_names)
    for sheet in xl.sheet_names:
        print(f"\n--- Sheet: {sheet} ---")
        df = xl.parse(sheet).head(15)
        print(df.to_string(index=False))
except Exception as e:
    print("Error reading excel:", e)
