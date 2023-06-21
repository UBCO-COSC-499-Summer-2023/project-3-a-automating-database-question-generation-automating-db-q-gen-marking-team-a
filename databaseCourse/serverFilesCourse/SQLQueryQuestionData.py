# Reads a file and return an array of its lines
def readFileLines(filePath):
    
    # Opens the file at the given path
    textfile = open(filePath, "r")

    # Reads and split over each line
    lines = textfile.read().splitlines()

    # Closes file
    textfile.close()

    # Returns an array of the lines
    return lines

# Places the database text into data as a parameter
# Places the correct answer into data as a correct answer
def generateQuestionData(data, questionNumber):

    # Reads and sets the database text
    data["params"]["ddl"] = readFileLines(data["params"]["databaseSchemaFile"])

    # Reads and sets the appropriate solution
    # Pass in the question number, but subtract one to map it to array indexes
    data["correct_answers"]["SQLEditor"] = readFileLines(data["params"]["databaseAnswerFile"])[questionNumber - 1]
    