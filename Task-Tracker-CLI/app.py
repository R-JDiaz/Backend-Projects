import sys
import os
from task import TaskManager
from fileHandler import FileHandler

def showInstructions():
    print("Usage:")
    print("  python app.py add <task>")
    print("  python app.py delete <task_number>")
    print("  python app.py mark <status> <number>")
    print("  python app.py list <status>[optional]")
    print("  python app.py update <task_number> <updated_definition>")

def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

def main(filePath):
    fHandler = FileHandler(filePath)
    print(fHandler.filePath)
    print(fHandler.fileType)

    def save():
        fHandler.overwriteFile(manager.tasks)
        print("Saved Succesfully")

    def valueGetter(argIndex):
        words = args[argIndex:len(args)]
        return " ".join(words)
        
        

    args = sys.argv

    tasks = fHandler.getFileData()
    manager = TaskManager(tasks)
    fHandler.checkIfFileExists()
    clear()
    

    if len(args) < 2:
        showInstructions()
        return
    
    command = args[1]
    
    if command == "add" :
        if manager.checkIfExist(valueGetter(2)) == False:
            print(manager.createTask(valueGetter(2)))
            print(valueGetter(2))
            save()
        else:
            print("Task already CREATED")
            
    
    elif command == "delete":
        print(manager.deleteTask(valueGetter(2)))
        save()

    elif command == "update":
        print(manager.updateTaskAttribute(args[2],"definition", valueGetter(3)))
        save()

    elif command == "mark":
        print(manager.updateTaskAttribute(args[3],"status", args[2]))
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
        
