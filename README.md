# finalexam-questionconverter-py
This script converts exam questions collected by finalexam-questioncollector-js to a txt format which can be imported into Anki. The script requires 
This tool was made to be used with https://github.com/greekdoctor/finalexam-questioncollector-js. See the readme of that repository for more details.

## Usage
`python ./QuestionConverter.py [inputfile]`

This will output a .txt file which can be imported into Anki. Upon importing, check [Allow HTML in fields] for proper formatting. Anki should autodetect that fields are separated by tab.

To separate questions by subcategory and category, you can separate the source material (from questioncollector) into separate documents by subcategory and category.

## Known bugs
The script parses the questions based on rigid rules, more specifically that blank newlines either separate one question from the next or the answer and explanation from the question stem. If the document to parse contains blank newlines other than this, all preceding questions will be fucked up in the output. As it stands, finalexam-questioncollector-js does input random blank newlines now and then, and so manual correction of these is necessary for questionconverter to function properly. Reading through the whole output of questioncollector is unfeasible, but you'll know that this has happened when Anki outputs warnings or errors when importing the output of questionconverter.
A much better solution would've been to use some clever regex, but I'm not that clever.
