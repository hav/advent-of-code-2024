from pathlib import Path

def sanitizeInputFile(inputFile):
    with Path(inputFile).open('r') as file:
        return file.readlines()

def sanitizeInput(inputData):
    