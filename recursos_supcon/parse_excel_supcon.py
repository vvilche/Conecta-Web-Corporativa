import pandas as pd

file_path = "SUPCON Oversea Product List (1).xlsx"
output_path = "parsed_catalog.txt"

try:
    xl = pd.ExcelFile(file_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Sheets available: {xl.sheet_names}\n")
        f.write("="*50 + "\n")
        for sheet in xl.sheet_names:
            f.write(f"\n--- Sheet: {sheet} ---\n")
            df = xl.parse(sheet).head(50)
            f.write(df.to_string(index=False))
            f.write("\n")
    print(f"Extraction successful. Saved to {output_path}")
except Exception as e:
    print("Error reading excel:", e)
