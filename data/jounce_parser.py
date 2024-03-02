from jouvence.parser import JouvenceParser
from jouvence.html import HtmlDocumentRenderer,BaseDocumentRenderer
parser = JouvenceParser()
document = parser.parse("/home/nikhil/Documents/Github/movie-screenplay-parser/data/brick.fountain")
print(document.scenes)
for i in document.scenes:
    print(dir(i))