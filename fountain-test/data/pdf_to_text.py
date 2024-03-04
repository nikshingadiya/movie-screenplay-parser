from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextLineHorizontal

def extract_text_with_coordinates(pdf_path):
    """Extracts text from a PDF file along with their coordinates.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: List of tuples containing text and their coordinates.
    """
    text_with_coordinates = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    if isinstance(text_line, LTTextLineHorizontal):
                        text = ''
                        for character in text_line:
                            if isinstance(character, LTChar):
                                text += character.get_text()
                        # Get bounding box
                        x0, y0, x1, y1 = text_line.bbox
                        text_with_coordinates.append((text, (x0, y0, x1, y1)))
                    else:
                        # Non-text elements
                        # Get bounding box
                        x0, y0, x1, y1 = element.bbox
                        text_with_coordinates.append(('Non-text element', (x0, y0, x1, y1)))
    return text_with_coordinates

def write_extracted_text_with_coordinates_to_file(pdf_path, output_file):
    extracted_text_with_coordinates = extract_text_with_coordinates(pdf_path)
    with open(output_file, 'w') as file:
        for text, coordinates in extracted_text_with_coordinates:
            file.write(f"{text} @ Coordinates: {coordinates}\n")

# Example usage
pdf_path = "iron-man-2008.pdf"  # Replace with your actual PDF file path
output_file = "extracted_text_with_coordinates.txt"  # Replace with desired output file path
write_extracted_text_with_coordinates_to_file(pdf_path, output_file)
print("Text with coordinates written to", output_file)
