import re
from parse_las import find_uppgifter_and_extract


def extract_text_from_pages(pages, pdf):
    text = ""
    for page_number in pages:
        page = pdf.pages[page_number]
        text += page.extract_text() + "\n"
    return text


def parse_ord(reader, pages):
    # Extract and clean the text
    full_text = "\n".join(
        reader.pages[page_no].extract_text() for page_no in pages
    ).splitlines()
    full_text = [line.strip() for line in full_text if line.strip()]

    # Regex patterns
    question_pattern = re.compile(r"(\d+)\.\s+([\w\s]+)\s+(\d+)\.\s+([\w\s]+)")
    option_pattern = re.compile(r"([A-E])\s+([\w\s]+)\s+([A-E])\s+([\w\s]+)")

    qa_data, current_answers_1, current_answers_2 = [], {}, {}

    for line in full_text:
        if q_match := question_pattern.match(line):
            if current_answers_1:
                qa_data.extend(
                    [
                        {
                            "question_number": int(current_question_number_1),
                            "question": current_question_text_1,
                            "answers": current_answers_1,
                            "question_type": "ORD",
                        },
                        {
                            "question_number": int(current_question_number_2),
                            "question": current_question_text_2,
                            "answers": current_answers_2,
                            "question_type": "ORD",
                        },
                    ]
                )

            (
                current_question_number_1,
                current_question_text_1,
                current_question_number_2,
                current_question_text_2,
            ) = map(str.strip, q_match.groups())
            current_answers_1, current_answers_2 = {}, {}

        elif o_match := option_pattern.match(line):
            current_answers_1[o_match.group(1)] = o_match.group(2).strip()
            current_answers_2[o_match.group(3)] = o_match.group(4).strip()

    if current_answers_1:
        qa_data.extend(
            [
                {
                    "question_number": int(current_question_number_1),
                    "question": current_question_text_1,
                    "answers": current_answers_1,
                    "question_type": "ORD",
                },
                {
                    "question_number": int(current_question_number_2),
                    "question": current_question_text_2,
                    "answers": current_answers_2,
                    "question_type": "ORD",
                },
            ]
        )
    qa_data = sorted(qa_data, key=lambda x: x["question_number"])

    return qa_data


def parse_las(reader, pages):
    # Placeholder function for parsing LÄS section
    # Extract and clean the text from the specified pages
    extracted_questions = find_uppgifter_and_extract(reader, pages)
    return extracted_questions


def parse_mek(reader, pages):
    question_list = []

    for page_num in pages:  # page number indexing starts from 0
        page = reader.pages[page_num]

        text_box = (
            0,
            0,
            page.width,
            page.height - 50,
        )  # A box excluding the bottom 50 points of the page
        cropped_page = page.within_bbox(text_box)

        text = cropped_page.extract_text()

        # Split text into lines
        lines = text.split("\n")
        question_num = None
        question_text = ""
        answer_options = {}

        for line in lines:
            # Check if the line starts with a question number (i.e., a number followed by a dot)
            match = re.match(r"^(\d{1,2})\.\s*(.*)", line)
            if match:
                # Store the previous question and its answers before moving to the next question
                if question_num and answer_options:
                    question_list.append(
                        {
                            "question_number": int(question_num),
                            "question": re.sub(r"\s+", " ", question_text),
                            "answers": answer_options,
                            "question_type": "MEK",
                        }
                    )

                # Start a new question
                question_num = match.group(1)
                question_text = match.group(2)
                answer_options = (
                    {}
                )  # Reset answer options as a dict now (e.g., {'a': '...', 'b': '...'})
            elif re.match(
                r"^[A-D]\s+", line
            ):  # If the line starts with A, B, C, or D (indicating an answer option)
                option_letter = line[
                    0
                ].lower()  # Convert 'A', 'B', 'C', 'D' to 'a', 'b', 'c', 'd'
                option_text = re.sub(
                    r"\s+", " ", line[2:]
                )  # Extract the text after the letter and space
                answer_options[option_letter] = option_text
            else:
                # Continue building the question text if it's multi-line
                question_text += " " + line.strip()

        # Store the last question
        if question_num and answer_options:
            question_list.append(
                {
                    "question_number": int(question_num),
                    "question": re.sub(r"\s+", " ", question_text),
                    "answers": answer_options,
                    "question_type": "MEK",
                }
            )

    return question_list


verb_parse_methods = {
    # "ORD": parse_ord, ## commented out because they are already part of the repo
    "LÄS": parse_las,
    "MEK": parse_mek,
}
