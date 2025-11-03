from datetime import datetime

class TaskManager:
    def __init__(self, tasks):
        self.tasks = tasks

    def checkIfExist(self, description):
        words = description.split()
        for k in self.tasks:
            for w in words:
                if w in self.tasks[k]['description']:
                    return True
            if description in self.tasks[k]['description']:
                return True
        return False
    
    def createTask(self, description, status="todo"): 
        curDateTime = datetime.now()
        dateString = curDateTime.strftime("%Y-%m-%d %H:%M:%S")
        newTask = Task(max(len(self.tasks) + 1, 0), description, status, dateString, dateString)
        self.tasks[newTask.id] = {"status" : newTask.status, 
                                "description" : newTask.description, 
                                "createdAt" : newTask.createdAt, 
                                "updatedAt" : newTask.updatedAt}
        return 'Created Succesfully'
    
    def deleteTask(self,id):
        if id in self.tasks.keys():
            self.tasks.pop(id)
            return f"TASK ID: {id} DELETED SUCCESFULLY"
        else:
            return f"TASK ID: {id} NOT FOUND"

    def updateTaskAttribute(self, id, attribute, value):
        if id in self.tasks:
            self.tasks[id][attribute] = value
            curDateTime = datetime.now()
            dateString = curDateTime.strftime("%Y-%m-%d %H:%M:%S")
            self.tasks[id]["updatedAt"] = dateString
            return 'Task Updated Succesfully'
        else:
            return 'Id not FOUND'

    def getTasks(self):
        for task in self.tasks:
                print(f"Id: {task}")
                print(f"Task: {self.tasks[task]['description']}")
                print(f"Status: {self.tasks[task]['status']}")
                print(f"UpdateAt: {self.tasks[task]['updatedAt']}")
                print(f"CreatedAt: {self.tasks[task]['createdAt']}")
                print(" ")

    def getTasksByStatus(self, status):
        for task in self.tasks:
            if self.tasks[task].status == status:
                print(f"Id: {task}")
                print(f"Task: {self.tasks[task]['description']}")
                print(f"Status: {self.tasks[task]['status']}")
                print(" ")

    def getIdByDefinition(self, definition):
        for k,v in self.tasks.items():
            if self.tasks[v]["definition"] == definition:
                return k
        
    def toDict(self):
        return self.tasks

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id 
        self.description = description
        self.status = status #('todo', 'in-progress', 'done)
        self.createdAt = createdAt #date and time the task was created
        self.updatedAt = updatedAt #date and time the tasl was last updated