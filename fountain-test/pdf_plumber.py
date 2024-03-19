import argparse
import pdfplumber

def slicer(my_str, subs):
    indices = [my_str.find(sub) for sub in subs]
    indices = [i for i in indices if i != -1]
    if indices:
        index = min(indices)
        return my_str[index:] 
    else:
        return my_str
    
def is_all_digits(text):
    text=text.replace(".","")
    return all(char.isdigit() for char in text)

def extract_text_from_pdf(pdf_path,char_height = 12):
    with pdfplumber.open(pdf_path) as pdf:
        output_text = ''
        for page_number in range(len(pdf.pages)):
            first_page = pdf.pages[page_number]  # Assuming you want to work with the first page (0-based index)
            text_lines = first_page.extract_text_lines()
            for i, line in enumerate(text_lines):
                # Calculate distance between current line and previous line
                distance = line["top"] - text_lines[i - 1]["top"]
                if distance > char_height:
                    output_text += "\n\n\n" + slicer(line['text'], ['INT', 'EXT'])
                else:
                    output_text += "\n" + line["text"]  # Add a space between each line
            output_text +="\n\n\n\n"+f'page_number={page_number+1}'+"\n"
    return output_text

def write_text_to_file(output_text, file_path):
    with open(file_path, "w") as file:
        file.write(output_text)

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF and save it as a Fountain file.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file")
    args = parser.parse_args()

    pdf_path = args.pdf_path
    output_text = extract_text_from_pdf(pdf_path, char_height=12)

    output_file = pdf_path.split("/")[-1].split(".")[0]
    folder_path = "./fountain_file/"
    output_file = folder_path + output_file + ".fountain"
    write_text_to_file(output_text, output_file)
    print(f"Text extracted from {pdf_path} and saved to {output_file}")

if __name__ == "__main__":
    main()
