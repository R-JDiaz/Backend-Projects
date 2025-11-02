from datetime import datetime

class TaskManager:
    def __init__(self, tasks):
        self.tasks = tasks

    def createTask(self, description, status="todo"): 
        curDateTime = datetime.now()
        dateString = curDateTime.strftime("%Y-%m-%d %H:%M:%S")
        newTask = Task(max(len(self.tasks) + 1, 0), description, status, dateString, dateString)
        self.tasks[newTask.id] = {"status" : newTask.status, 
                                  "description" : newTask.description, 
                                  "createdAt" : newTask.createdAt, 
                                  "updatedAt" : newTask.updatedAt}
        return f"Task added succesfully (ID: {newTask.id})"
    
    def deleteTask(self,id):
        if id in self.tasks.keys():
            self.tasks.pop(id)
        else:
            print(f"TASK ID: {id} NOT FOUND")
    
    def updateTaskStatus(self, id, status): 
        self.tasks[id]['status'] = status

    def getTasks(self):
        for task in self.tasks:
                print(f"Id: {task}")
                print(f"Task: {self.tasks[task]['description']}")
                print(f"Status: {self.tasks[task]['status']}")
                print(" ")


    def getTasksByStatus(self, status):
        for task in self.tasks:
            if self.tasks[task].status == status:
                print(f"Id: {task}")
                print(f"Task: {self.tasks[task]['description']}")
                print(f"Status: {self.tasks[task]['status']}")
                print(" ")

    def toDict(self):
        return self.tasks

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id 
        self.description = description
        self.status = status #('todo', 'in-progress', 'done)
        self.createdAt = createdAt #date and time the task was created
        self.updatedAt = updatedAt #date and time the tasl was last updated