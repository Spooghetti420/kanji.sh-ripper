import requests
import os
import time

try:
    os.mkdir("frequency")
except FileExistsError:
    print("frequency directory already exists...")

for i in range(1, 21):
    filename = f"{50*(i-1)+1}-{50*i}"
    pdf_name = f"F{i}"

    if os.path.exists(fp := os.path.join("frequency", f"{filename}.pdf")):
        print(f"Skipping existing file {filename}...")
        continue

    req_pdf = requests.get(f"https://kanji.sh/api/download?path=next/pdf/frequency/{filename}.pdf&name={pdf_name}")

    if req_pdf.ok:
        with open(fp, mode="wb") as f:
            f.write(req_pdf.content)
        print(f"Saved file {filename}.pdf")
    else:
        print(f"Unable to access file {filename}.pdf.")
    time.sleep(1)