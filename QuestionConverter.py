#Plan:
#1. Create a blank text document "AnkiList"
#2. Locate the first line beginning with the three letter code for the subject ("FOG - ") and the previous line is blank
#3. Append the first line ("FOG - 3") to AnkiList
#4. Append <br> to AnkiList
#5. Append the next line of inputFile to AnkiList
#6. Append <br> to AnkiList
#7. Repeat #5 and #6 until the next line is "ANSWER"
#8. Append [tabulator character] to AnkiList
#9. Append the next line to AnkiList
#10. Append <br> to AnkiList
#11. Repeat #9 and #10 until the next line begins with the three letter code
#12. Proceed to new line in AnkiList
#13. Repeat #2 - #12
import os
import sys
from pathlib import Path

# Opening the input file
inputFileName = sys.argv[1]
inputFile = open(inputFileName, mode="r", encoding="utf-8")

# Opening the first output file
outputFileName1 = "unformatted output.txt"
outputFile1 = open("./" + outputFileName1, mode="w", encoding="utf-8")

# Opening the second output file
inputFileNameWithoutPath = os.path.basename(inputFileName)
p = Path(inputFileNameWithoutPath)
outputFileName2 = "{0}_ExportToAnki.txt".format(p.stem)
outputFile2 = open("./" + outputFileName2, mode="w", encoding="utf-8")

#1. Create a blank text document "AnkiList"
#2. Append the first line ("FOG - 2") and <br> to AnkiList
#3. Append the next line and <br> of inputFile to AnkiList
#4. Repeat #2 and #3 until the previous line is blank (at this point we've reached the answers)
#5. Append [tabulator character] and the next line and <br> to AnkiList
#6. Repeat #5 until the previous line is blank again (at this point we've reached the end of the answers)
#7. Proceed to new line in AnkiList
#8. Repeat #2 - #7

# Loops through the file
previousLine = "l"
count = 0
currentlyInAnswer = False

for line in inputFile:
	count += 1
	currentLine = "{1}".format(count, line.strip())

	if (previousLine != "") and (currentLine != ""):
		outputFile1.write((currentLine) + "<br>")

	elif (previousLine == "") and (currentlyInAnswer == False):
		outputFile1.write("	" + currentLine + "<br>")
		currentlyInAnswer = True
		previousLine = currentLine

	elif (previousLine == "") and (currentlyInAnswer == True):
		outputFile1.write("\n" + currentLine + "<br>")
		currentlyInAnswer = False
	
	previousLine = currentLine


# Opening the first output file, this time to read
outputFile1 = open("./" + outputFileName1, mode="r", encoding="utf-8")

# Loops through the file again to make certain minor adjustments to the formatting to make Anki happy
count = 0
for line in outputFile1:
	count += 1
	currentLine = "{1}".format(count, line.strip())
	newCurrentLine = currentLine.replace(")  	", ")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
	newCurrentLine2 = newCurrentLine.replace(" - 	", " -  ")
	newCurrentLine3 = newCurrentLine2.replace("	- ", "    - ")
	outputFile2.write(newCurrentLine3 + "\n")