import tika
from tika import parser

tika.initVM()

# Parse the PDF file
parsed = parser.from_file('/home/nikhil/Documents/Github/movie-screenplay-parser/data/Interstallar.pdf')

# Extract metadata
metadata = parsed["metadata"]
print("Metadata:", metadata)

# Extract content
content = parsed["content"]
print("Content:", content)

# Save content to a file
output_file_path = '/home/nikhil/Documents/Github/movie-screenplay-parser/data/Interstallar_content.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Content saved to:", output_file_path)
print(content)
