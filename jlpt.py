import requests
import os
import time

try:
    os.mkdir("jlpt")
except FileExistsError:
    print("jlpt directory already exists...")

for i in range(1, 6):
    filename = f"n{i}"
    pdf_name = f"N{i}"

    if os.path.exists(fp := os.path.join("jlpt", f"{filename}.pdf")):
        print(f"Skipping existing file {filename}...")
        continue

    req_pdf = requests.get(f"https://kanji.sh/api/download?path=next/pdf/jlpt/{filename}.pdf&name={pdf_name}")

    if req_pdf.ok:
        with open(fp, mode="wb") as f:
            f.write(req_pdf.content)
        print(f"Saved file {filename}.pdf")
    else:
        print(f"Unable to access file {filename}.pdf.")
    time.sleep(1)