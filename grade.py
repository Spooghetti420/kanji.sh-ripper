import requests
import os
import time

try:
    os.mkdir("grade")
except FileExistsError:
    print("grade directory already exists...")

for i in range(1, 7):
    filename = f"g{i}"
    pdf_name = f"G{i}"

    if os.path.exists(fp := os.path.join("grade", f"{filename}.pdf")):
        print(f"Skipping existing file {filename}...")
        continue

    req_pdf = requests.get(f"https://kanji.sh/api/download?path=next/pdf/grade/{filename}.pdf&name={pdf_name}")

    if req_pdf.ok:
        with open(fp, mode="wb") as f:
            f.write(req_pdf.content)
        print(f"Saved file {filename}.pdf")
    else:
        print(f"Unable to access file {filename}.pdf.")
    time.sleep(1)