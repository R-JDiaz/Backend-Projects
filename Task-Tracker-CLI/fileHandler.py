from pathlib import Path
import json
import re

class FileHandler:
    def __init__(self, filePath):
        self.filePath = filePath
        self.fileType = self.getFileType()

    def getFileType(self):
        pattern = r"\.([a-zA-Z0-9]+)$"
        match = re.search(pattern,self.filePath)
        if match:
            return match.group(1)
        else:
            print("Invalid File Path")
    
    def checkIfFileExists(self):
        file = Path(self.filePath)
        if not file.exists():
            with open(f"Tasks.{self.fileType.lower()}", "x") as f:
                f.write("{ }")
                return True
        else:
            return False
    
    def getFileData(self):
        if self.checkIfFileExists() == False:
            with open(self.filePath, 'r') as file:
                return json.load(file)
        else:
            return { }

    def overwriteFile(self, data):
        if self.checkIfFileExists() == False:
            with open(self.filePath, "w") as f:
                json.dump(data, f)
                return f"File Succesfully OverWrited"
        else:
            return f"File: {self.filePath} Not Found"
    