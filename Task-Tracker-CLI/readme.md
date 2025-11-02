#TASK TRACKER
My solutions for the task-tracker challenge from roadmap.sh

#How to Run
Clone the Repository and run the following command:
https://github.com/R-JDiaz/Backend-Projects/Task-Tracker-CLI
cd Backend-Projects/Task-Tracker

python app.py #to run the program and show the available commands

#to add a task
python app.py add "Read a Book" 

#to delete a task
python app.py delete <task-number>

#to mark the status of a task
python app.py mark <status> <task-number>

#to show the available tasks
python app.py list

#to show the available tasks depending the status
python app.py list <status>
