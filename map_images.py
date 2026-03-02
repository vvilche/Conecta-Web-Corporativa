import openpyxl
from openpyxl_image_loader import SheetImageLoader
import os

wb = openpyxl.load_workbook("recursos_supcon/SUPCON Oversea Product List (1).xlsx", data_only=True)

for sheet_name in wb.sheetnames:
    print(f"--- Sheet: {sheet_name} ---")
    ws = wb[sheet_name]
    try:
        from openpyxl.drawing.image import Image
        print(f"Images in sheet: {len(ws._images)}")
        for img in ws._images:
            # openpyxl 3.0+ image anchor
            if hasattr(img.anchor, '_from'):
                row = img.anchor._from.row
                col = img.anchor._from.col
            elif hasattr(img.anchor, 'from_'): # Older versions
                row = img.anchor.from_.row
                col = img.anchor.from_.col
            else:
                row = "Unknown"
                col = "Unknown"
                
            print(f"Image mapped to Row: {row}, Col: {col}")
    except Exception as e:
        print(f"Error reading images in {sheet_name}: {e}")
