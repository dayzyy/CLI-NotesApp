# Task Manager CLI Application

Using this application you can **create**, **update** and **delete** tasks. Afterwards you can display them and keep track of the things you have to do. :D  
Each task has an **ID**, the **text**(note) and a **status**, which tells you if the task is **todo/done/in-progress**.

## Features
- Add new tasks.
- Update task notes.
- Delete tasks.
- Mark tasks with statuses.
- List tasks based on their status.

## Prerequisites
- **Python 3.6+**

## Setup
1. Clone the repository:
```
git clone https://github.com/dayzyy/CLI-NotesApp.git
```

## Commands

```python
# To add a task
python3 manage.py add <note>

# Example
python3 manage.py add "Wash the dishes"


# To update a task
python3 manage.py update <id> <note>

# Example
python3 manage.py update 1 "Wash the dishes and mop the floor"


# To delete a task
python3 manage.py delete <id>

# Example
python3 manage.py delete 1


# To mark a task as in -- todo/done/in-progress.
python3 manage.py mark <id> <status>

# Examples
python3 manage.py mark 1 todo
python3 manage.py mark 1 done
python3 manage.py mark 1 in-progress


# To list the tasks with provied status
python3 manage.py list <status>

# If you leave the status arguement empty like in the first example below, it will list all the tasks no matter their status

# Examples
python3 manage.py list
python3 manage.py list todo
python3 manage.py list done
python3 manage.py list in-progress
```

##### Inspired By
https://roadmap.sh/projects/task-tracker
