import io
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LAParams, LTContainer, LTTextLine

def extract_text_with_layout(pdf_path):
    """Extracts text from a PDF file while preserving original layout and whitespace.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        tuple:
            - str: Extracted text with preserved layout and whitespace.
            - tuple: (page_height, page_width) of the PDF file.
    """

    # Set parameters to preserve whitespace and layout while extracting text
    laparams = LAParams(char_margin=0, word_margin=0, line_margin=0)

    # Extract text with layout elements
    extracted_text_with_layout = ""
    page_height, page_width = 0, 0
    for page_layout in extract_pages(pdf_path, laparams=laparams):
        for obj in page_layout:
            if isinstance(obj, LTContainer):
                for text_line in obj:
                    if isinstance(text_line, LTTextLine):
                        # Append lines with surrounding layout context
                        extracted_text_with_layout += text_line.__repr__() + "\n"
                    else:
                        # Include non-text elements for context preservation
                        extracted_text_with_layout += obj.__repr__() + "\n"
            else:
                # Account for other potential page layout elements
                extracted_text_with_layout += obj.__repr__() + "\n"

        page_height = page_layout.height
        page_width = page_layout.width

    # Extract text only (optional, depending on your needs)
    extracted_text_only = extract_text(pdf_path, laparams=laparams)

    return extracted_text_with_layout, (page_height, page_width), extracted_text_only

# Example usage
pdf_path = "iron-man-2008.pdf"  # Replace with your actual PDF file path
extracted_text_with_layout, page_dim, extracted_text_only = extract_text_with_layout(pdf_path)

print("Text with layout and whitespace:")
print(extracted_text_with_layout)

print("\nPage dimensions:", page_dim)

print("\nText only (optional):")
print(extracted_text_only)
