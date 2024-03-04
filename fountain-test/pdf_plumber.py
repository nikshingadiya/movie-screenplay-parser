import pdfplumber

def slicer(my_str, subs):
    indices = [my_str.find(sub) for sub in subs]
    indices = [i for i in indices if i != -1]
    if indices:
        index = min(indices)
        return my_str[index:] 
    else:
        return my_str

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

# Usage example:
pdf_path = "./data/Imitation+Game.pdf"
output_text = extract_text_from_pdf(pdf_path,char_height = 12)

def write_text_to_file(output_text, file_path):
    with open(file_path, "w") as file:
        file.write(output_text)
output_file=pdf_path.split("/")[-1].split(".")[0]
output_file=output_file+".fountain"
write_text_to_file(output_text, output_file)
