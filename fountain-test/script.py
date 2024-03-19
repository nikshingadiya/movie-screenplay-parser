import os
import subprocess
from pdf_plumber import  extract_text_from_pdf

def main():
    # Loop through all PDF files in the ./data/ directory
    for filename in os.listdir("./data/"):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join("./data/", filename)
            output_text = extract_text_from_pdf(pdf_path)
            
            # Write the extracted text to a Fountain file
            output_file = os.path.join("./fountain_file/", os.path.splitext(filename)[0] + ".fountain")
            with open(output_file, "w") as file:
                file.write(output_text)
            print(f"Text extracted from {pdf_path} and saved to {output_file}")

            # Call the Node.js script to parse the Fountain file
            subprocess.run(["node", "index.js", output_file])

if __name__ == "__main__":
    main()
