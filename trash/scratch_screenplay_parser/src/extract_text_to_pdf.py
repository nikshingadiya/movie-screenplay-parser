import PyPDF2
def extract_text_from_pdf(pdf_path):
    whole_text=""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Iterate through each page and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            whole_text+=text
            
            # You can process the extracted text as needed (print, store, etc.)
            # print(f"Page {page_num + 1}:\n{text}\n")
        print("extraction raw")

        return whole_text

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = 'pacific-rim-2013_1.pdf'
whole_text=extract_text_from_pdf(pdf_file_path)
