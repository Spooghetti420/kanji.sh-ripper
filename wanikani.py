import requests
import os
import time

try:
    os.mkdir("wanikani")
except FileExistsError:
    print("wanikani directory already exists...")

for i in range(1, 61):
    filename = f"WK {i}"

    if os.path.exists(fp := os.path.join("wanikani", f"{filename}.pdf")):
        print(f"Skipping existing file {filename}...")
        continue

    req_pdf = requests.get(f"https://kanji.sh/api/download?path=next/pdf/wanikani/{i}.pdf&name=WK%20{i}")

    if req_pdf.ok:
        with open(fp, mode="wb") as f:
            f.write(req_pdf.content)
        print(f"Saved file {filename}.pdf")
    else:
        print(f"Unable to access file {filename}.pdf.")
    time.sleep(1)
