import requests
import os
import time

try:
    os.mkdir("kanji_garden")
except FileExistsError:
    print("kanji_garden directory already exists...")

for i in range(1, 53):
    filename = f"{50*(i-1)+1}-{50*i}"
    pdf_name = f"KG{i}"

    if os.path.exists(fp := os.path.join("kanji_garden", f"{filename}.pdf")):
        print(f"Skipping existing file {filename}...")
        continue

    req_pdf = requests.get(f"https://kanji.sh/api/download?path=next/pdf/kanjigarden/{filename}.pdf&name={pdf_name}")

    if req_pdf.ok:
        with open(fp, mode="wb") as f:
            f.write(req_pdf.content)
        print(f"Saved file {filename}.pdf")
    else:
        print(f"Unable to access file {filename}.pdf.")
    time.sleep(1)

# Final PDF is different, because it ends at 2645 instead of 2650.
if os.path.exists(fp:= os.path.join("kanji_garden", "2601-2645.pdf")):
    print("Skipping file 2601-2645.pdf")
    raise SystemExit()

req_final = requests.get("https://kanji.sh/api/download?path=next/pdf/kanjigarden/2601-2650.pdf&name=KG53")
if req_final.ok:
    with open(fp, mode="wb") as f:
        f.write(req_final.content)
    print("Saved file 2601-2645.pdf")
else:
    print("Unable to access file 2601-2645.pdf.")
