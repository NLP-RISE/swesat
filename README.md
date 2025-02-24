# SweSAT-1.0: A Benchmark for Swedish LLMs

SweSAT-1.0 is a benchmark dataset created from the Swedish university entrance exam (*Högskoleprovet*) to assess large language models (LLMs) in Swedish. It includes **867 multiple-choice questions** from the last 8 exams (2020-10-25 to 2024-04-13), covering  the following six different question types: 

- **ORD** (Vocabulary) - Tests the understanding of in-domain words and synonyms.
- **LÄS** (Reading Comprehension) - Assesses the ability to make inferences from a text.
- **MEK** (Sentence Completion) - Evaluates the ability to complete sentences via cloze tests.
- **XYZ** (Mathematical Problem-Solving) - Includes questions on arithmetic, algebra, geometry, statistics, and functions.
- **KVA** (Quantitative Comparisons) - Measures the ability to compare quantities in mathematical concepts.
- **NOG** (Data Sufficiency) - Determines the ability to assess whether given data is sufficient to solve a problem.


## Dataset

The Swe-SAT-1.0 dataset is partially available [exams](exams) with the exception of reading passages for the LÄS section. To obtain the full dataset including the LÄS section, follow these steps:

- Obtain the LÄS section PDFs from [studera.nu](https://www.studera.nu/hogskoleprov/forbered/tidigare-hogskoleprov/) for each year, which can be found under _"Prov och facit"_. This PDFs for the LÄS section all end in `-verb-utan-elf.pdf` for all years.

- Create a new directory `exam_pdfs` and place the downloaded PDFs inside in the following format:

  ```shell
  ├── exam_pdfs
  │   ├── 2023-10-22
  │   │   └── provpass-3-verb-utan-elf.pdf
  │   └── 2024-04-13
  │       └── provpass-4-verb-utan-elf.pdf
  ```

  > [!IMPORTANT]  
  > The structure of the `exam_pdf` directory where the downloaded PDFs land **must** correspond to the structure in [`exams`](exams)


- Install `pdfplummer` (this is the only required dependency):

  ```shell
  # in your virtual environment
  pip3 install pdfplumber
  ```

- Run the script to process the verbal sections
  
  ```shell
    python3 process_verbal_sections/parse_exam_pdf.py exam_pdfs
  ```

  > [!TIP]  
  > The LÄS section may contain copyrighted reading passages. You can inspect the sources of these passages on [studera.nu](https://www.studera.nu/hogskoleprov/forbered/tidigare-hogskoleprov/) for each exam year under _"Källor"_.


## Citation

If you use SweSAT-1.0 in your research, please cite:

```bib
@article{SweSAT2024,
  title={SweSAT-1.0: The Swedish University Entrance Exam as a Benchmark for Large Language Models},
  author={Kurfalı, Murathan and Zahra, Shorouq and Gogoulou, Evangelia and Dürlich, Luise and Carlsson, Fredrik and Nivre, Joakim},
  booktitle = "Proceedings of The Joint 25th Nordic Conference on Computational Linguistics and 11th Baltic Conference on Human Language Technologies (NoDaLiDa/Baltic-HLT 2025)",
  month = march,
  year = "2025",
  address = "Talinn, Estonia"
}
```
