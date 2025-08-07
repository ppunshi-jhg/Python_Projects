import re
from PyPDF2 import PdfReader
from collections import Counter

def extract_text_from_PDF(pdf_path: str) -> list[str]:
    with open(pdf_path, "rb") as pdf:
        reader = PdfReader(pdf, strict = False) #What strict does is it allows the reader to read PDFs that may not conform to the strict PDF standards. So, it can handle some malformed PDFs.
        
        print(f"Number of pages in PDF: {len(reader.pages)}")
        print("-" * 50)
        
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        
    return pdf_text

def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text)
        # print(split_text)
        all_words += [word for word in split_text if word]
    
    return Counter(all_words)

def main():
    extracted_text: list[str] = extract_text_from_PDF("C:\\Users\\arora\\OneDrive - John Holland Group\\Github Repos\\Python Projects\\Basic_Projects\\Python_Projects\\sample.pdf")
    print(extracted_text) #The whole text on one page is returned as a single string. so there weill be only two elements in the list. because ther`e are only two pages in the PDF.
    # for text in extracted_text:
    #     print(text)
    
    # count_words(extracted_text)
    counter: Counter = count_words(extracted_text)
    print(counter.most_common(10))
    for word, count in counter.most_common(10):
        print(f"{word:10}: {count}")

if __name__ == "__main__":
    main()
