import pdfplumber
from re import compile
from sys import stderr
from concurrent.futures import ProcessPoolExecutor as PPE
from functools import partial

FILENAME = './data/Imitation+Game.pdf'
PATTERN = compile(r'(:  \d{5})')

# return a list of all lines that contain a match of the regular expression
def extract(filename, page):
    result = []
    try:
        with pdfplumber.open(filename) as pdf:
            for line in pdf.pages[page].extract_text().split('\n'):
                if PATTERN.search(line):
                    result.append(line)
    except Exception as e:
        print(e, file=stderr)
    return result

def main(filename):
    with PPE() as ppe, pdfplumber.open(filename) as pdf:
        for future in ppe.map(partial(extract, filename), range(len(pdf.pages))):
            print(future)

if __name__ == '__main__':
    main(FILENAME)