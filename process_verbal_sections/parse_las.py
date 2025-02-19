import json
import re


def postprocess(text):
    page_number_pattern = re.compile(r"–\s([1-9]|1[0-9]|2[0-9])\s")
    text = re.sub(page_number_pattern, '', text)

    text = text.replace("- ", "").replace(" –", "")
    text= text.replace("  ", "").replace(" \n", "\n")

    return text


def parse_question_string(question_string):
    """
    Parses the question string into structured data:
    question number, question text, and options as a dictionary.
    """
    # Regex to match question numbers (e.g., "17.", "18.", etc.)
    question_pattern = re.compile(r"(\d+)\.\s([^\n]+?)(?=\s[A-D]\s)", re.DOTALL)

    # Regex to match options (e.g., "A Some text", "B Some other text")
    option_pattern = re.compile(r"\s([A-D])\s([^\n]+?)(?=\s[A-D]\s|\s\d+\.\s|\Z)", re.DOTALL)

    parsed_questions = []

    # Find all questions with their numbers and text
    questions = question_pattern.findall(question_string)
    all_options = option_pattern.findall(question_string)

    # Process each question
    for q_no, question in enumerate(questions):
        question_number = question[0]  # The number of the question
        question_text = question[1].strip()  # The question text
        question_text = postprocess(question_text)
        # Extract the options after the question
        options = all_options[q_no*4:(q_no+1)*4]

        # Convert list of tuples to dictionary for options
        options_dict = {opt[0]: postprocess(opt[1].strip()) for opt in sorted(options)}

        # Append parsed question to the list
        parsed_questions.append({
            "question_number": int(question_number),
            "question": question_text,
            "answers": options_dict
        })

    return parsed_questions

def extract_text_from_columns(words, midpoint, page_height=None, y_limit=None, above=True):
    """Extract and merge text from left and right columns, optionally above or below a y_limit."""
    left_column = []
    right_column = []
    title_found=False
    word_id = 0
    for word in words:
        if above and 65< word['bottom'] <= y_limit or not above and word['bottom'] > y_limit:
            if page_height > word['bottom'] > page_height - 50:
                pass
            word_text = word['text'].replace("­", " ").strip()
            if word["size"] > 20 and word_id== 0:
                title_found = True
                word_text =  "Titel: " + word_text
                word_id = 1
            if word["size"] < 20 and title_found:
                word_text = "\n" + word_text
                title_found= False

            if word['x0'] < midpoint:
                left_column.append(word_text)
            else:
                right_column.append(word_text)
    merged =  " ".join(left_column) + " " + " ".join(right_column)
    merged = postprocess(merged.strip())
    return  merged


def find_uppgifter_and_extract(reader, pages):
    """Process PDF, find 'uppgifter', and extract passages and questions."""
    extracted_data = []
    ongoing_text = ""  # Holds ongoing passage text until "uppgifter" is found
    current_passage = None
    current_questions = ""

    for page_num in pages:
        page = reader.pages[page_num]
        words = page.extract_words(extra_attrs=["fontname", "size"])
        midpoint = page.width / 2
        uppgifter_found = False

        # Find y-coordinate of "uppgifter" or handle page without "uppgifter"
        for word in words:
            if word['text'].lower() == "uppgifter":
                uppgifter_found = True
                y_uppgifter = word['bottom'] - 0.5
                break

        if uppgifter_found:
            # Extract and merge text above "uppgifter"
            passage_text = extract_text_from_columns(words, midpoint, page_height=page.height, y_limit=y_uppgifter, above=True)
            ongoing_text += passage_text  # Continue from previous page if needed
            if current_passage is None:
                current_passage = ongoing_text  # Save the current passage text
            else:
                current_passage += " " + ongoing_text

            # Extract and merge text below "uppgifter" as questions
            question_text = extract_text_from_columns(words, midpoint,page_height=page.height, y_limit=y_uppgifter + 0.5, above=False)
            current_questions += question_text + " "

            # Save passage and corresponding questions as a pair
            extracted_data.extend(
                [
                    {**question, **{
                            "passage": postprocess(current_passage),
                            "question_type": 'LAS'
                        }}

                for question in parse_question_string(current_questions)]
            )

            # Reset for next passage and questions
            current_passage = None
            current_questions = ""
            ongoing_text = ""
        else:
            # Handle case where "uppgifter" is not found (passage may continue)
            page_bottom = page.height

            # Extract entire text from left and right columns
            page_text = extract_text_from_columns(words, midpoint, page_height=page.height, y_limit=page_bottom, above=True)
            ongoing_text = page_text

    return extracted_data


if __name__ == '__main__':
    # Path to your PDF file
    pdf_path = '/exam_pdfs/2023-03-25/provpass-3-verb-utan-elf.pdf'
    pdf_path = '/exam_pdfs/2024-04-13/provpass-4-verb-utan-elf.pdf'
    pdf_path = '/exam_pdfs/2023-10-22/provpass-5-verb_utan-elf.pdf'
    start_page = 3
    end_page = 7

    # Extract passages and questions
    extracted_data = find_uppgifter_and_extract(pdf_path, start_page, end_page)

    # Output the extracted passages and questions in JSON format
    output_json = json.dumps(extracted_data, ensure_ascii=False, indent=4)
    print(output_json)
