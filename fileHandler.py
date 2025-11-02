from pathlib import Path
import json

class FileHandler:
    @staticmethod
    def checkIfFileExists(filePath, fileType):
        file = Path(filePath)
        if not file.exists():
            with open(f"Tasks.{fileType.lower()}", "x") as f:
                f.write("{ }")
                return True
        else:
            return False
    
    @staticmethod
    def getFileData(filePath, fileType):
        if FileHandler.checkIfFileExists(filePath, fileType) == False:
            with open(filePath, 'r') as file:
                return json.load(file)
        else:
            return { }

    @staticmethod
    def overwriteFile(filePath, fileType, data):
        if FileHandler.checkIfFileExists(filePath, fileType) == False:
            with open(filePath, "w") as f:
                json.dump(data, f)
                return f"File Succesfully OverWrited"
        else:
            return f"File: {filePath} Not Found"
    