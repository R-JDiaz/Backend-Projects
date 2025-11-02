import sys
import os
from task import Task, TaskManager
from fileHandler import FileHandler

def main(filePath):
    def save():
        FileHandler.overwriteFile(filePath, fileType, manager.tasks)
        print("Saved Succesfully")

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    args = sys.argv
    
    fileType = "json"

    tasks = FileHandler.getFileData(filePath, fileType)
    manager = TaskManager(tasks)
    FileHandler.checkIfFileExists(filePath, fileType)
    clear()
    

    if len(args) < 2:
        print("Usage:")
        print("  python app.py add <task>")
        print("  python app.py delete <task_number>")
        print("  python app.py mark <status> <number>")
        print("  python app.py list <status>[optional]")
        return
    
    command = args[1]
    if command == "add" :
        print(manager.createTask(str(args[2])))
        save()
    
    elif command == "delete":
        print(manager.deleteTask(args[2]))
        save()

    elif command == "mark":
        print(manager.updateTaskStatus(args[3], args[2]))
        save()

    elif command == "list" and len(args) == 2:
        manager.getTasks()
    
    elif command == "list" and len(args) == 3:
        if args[2] in ["done", "todo", "in-progress"]:
            manager.getTasksByStatus(args[2])
        else:
            print("Invalid Status")
    else:
        print("Unknown Command")

if __name__ == "__main__":
    main("tasks.json")
        
