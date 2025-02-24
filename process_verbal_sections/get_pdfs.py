from pathlib import Path
import requests

pdf_paths = {
    "2020-10-25": {
        "provpass-4-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2020-10-25/hogskoleprovet-2020-10-25-del-4_verbal-del-utan-elf.pdf",
        "provpass-2-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2020-10-25/hogskoleprovet-2020-10-25-del-2_verbal-del-utan-elf.pdf",
    },
    "2021-05-08": {
        "provpass-4-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2021-05-08/provpass-4-verb-utan-elf.pdf",
        "provpass-1-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2021-05-08/provpass-1-verb-utan-elf.pdf",
    },
    "2021-10-24": {
        "provpass-2-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2021-10-24/211024-provpass-2-verb-utan-elf.pdf",
        "provpass-5-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2021-10-24/211024-provpass-5-verb-utan-elf.pdf",
    },
    "2022-03-12": {
        "provpass-4-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2022-03-12/provpass-4-verb-utan-elf.pdf",
        "provpass-2-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2022-03-12/provpass-2-verb-utan-elf.pdf",
    },
    "2022-10-23": {
        "provpass-2-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2022-10-23/provpass-2-verb-utan-elf.pdf",
        "provpass-5-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2022-10-23/provpass-5-verb-utan-elf.pdf",
    },
    "2023-03-25": {
        "provpass-3-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2023-03-25/provpass-3-verb-utan-elf.pdf",
        "provpass-5-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2023-03-25/provpass-5-verb-utan-elf.pdf",
    },
    "2023-10-22": {
        "provpass-3-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2023-10-22/provpass-3-verb-utan-elf.pdf",
        "provpass-5-verb_utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2023-10-22/provpass-5-verb_utan-elf.pdf",
    },
    "2024-04-13": {
        "provpass-1-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2024-04-13/provpass-1-verb-utan-elf.pdf",
        "provpass-4-verb-utan-elf.pdf": "https://www.studera.nu/globalassets/hogskoleprovet/hp-2024-04-13/provpass-4-verb-utan-elf.pdf",
    },
}

if __name__ == "__main__":
    Path("exam_pdfs").mkdir(parents=True, exist_ok=True)
    for datestamp in pdf_paths.keys():
        for pdf_filename in pdf_paths[datestamp].keys():
            print(datestamp, pdf_filename)
            url = pdf_paths[datestamp][pdf_filename]
            print(url)
            Path(f"exam_pdfs/{datestamp}").mkdir(parents=True, exist_ok=True)
            filename = Path(f"exam_pdfs/{datestamp}/{pdf_filename}")
            response = requests.get(url)
            print(f"Writing... {filename}")
            filename.write_bytes(response.content)
            print("Done!")
            print()
