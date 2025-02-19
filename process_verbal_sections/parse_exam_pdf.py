import glob
import json
import os
import sys

import pdfplumber
from verbal_utils import verb_parse_methods

verb_section_keywords = {
    "ORD": "ORD – Ordförståelse",
    "LÄS": "Svensk läsförståelse – LÄS",
    "MEK": "MEK – Meningskomplettering",
    "ELF": "ELF – Engelsk läsförståelse"
}

def identify_section_pages(pdf_path, section_keywords):
    section_pages = { k:[] for k in section_keywords}

    last_seen_section = None  # Track the last section identified
    reader = pdfplumber.open(pdf_path)

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()
        text = ' '.join(text.split())
        found_section = False

        # Check if the page belongs to any section
        for section, keyword in section_keywords.items():
            if keyword in text:
                section_pages[section].append(page_number)
                last_seen_section = section
                found_section = True
                #print(f"Section {section} found on page {page_number + 1}")
                break  # No need to check further if section is found

        # If no new section is found, it belongs to the last seen section
        if not found_section and last_seen_section:
            section_pages[last_seen_section].append(page_number)
            #print(f"Continuing Section {last_seen_section} on page {page_number + 1}")
    return section_pages


# Execute the main function
if __name__ == "__main__":
    exam_pdfs_path = sys.argv[1]
    pdf_files = sorted(glob.glob(f'{exam_pdfs_path}/*/*.pdf'))
    for pdf_path in pdf_files:
        output_path = pdf_path.replace('exam_pdfs', 'exams').replace('.pdf', '.json')
        os.makedirs('/'.join(output_path.split('/')[:-1]), exist_ok=True)
        if "verb" in pdf_path:
            print(pdf_path)

            # load the existing ORD questions & dismiss the rest
            exam = json.load(open(output_path, "r"))
            exam = [q for q in exam if q["question_type"] == "ORD"]

            section_pages = identify_section_pages(pdf_path, verb_section_keywords)
            print(section_pages)
            reader = pdfplumber.open(pdf_path)
            for k,parse_fcn in verb_parse_methods.items():
                questions = parse_fcn(reader, section_pages[k])
                if not questions: continue
                exam.extend(questions)
            with open(output_path, 'w') as f:
                f.write(json.dumps(exam, ensure_ascii=False, indent=4))
        else: # if facit or kvant in the pdf_path
            continue

