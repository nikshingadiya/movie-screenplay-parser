import pdftotext
from cleantext import clean

with open("./data/iron-man-2008.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Join the pages with double newline separation and remove indentation
text_with_double_newline = "\n\n".join(page for page in pdf)

# Write the text into a file
with open("pages_with_double_newline.txt", "w") as f:
    f.write(text_with_double_newline)

print("Text written into 'pages_with_double_newline.txt'")

