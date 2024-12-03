*** USEAGE ***

Using this application you can create, update and delete tasks. Afterwards you can display them and keep track of the things you have to do. :D
Each task has an ID, the text(note) and a status, which tells you if the task is todo/done/in-progress.

*** COMMANDS ***

# To add a task
python3 manage.py add <note>
e.g: python3 manage.py add "Wash the dishes"

# To update a task
python3 manage.py update <id> <note>
e.g: python3 manage.py update 1 "Wash the dishes and mop the floor"

# To delete a task
python3 manage.py delete <id>
e.g: python3 manage.py delete 1

# To mark a task as in -- todo/done/in-progress.
python3 manage.py mark <id> <status>
e.g: python3 manage.py mark 1 todo
e.g: python3 manage.py mark 1 done
e.g: python3 manage.py mark 1 in-progress

# To list the tasks with provied status (If you leave the status arguement empty like in the first example below, it will list all the tasks no matter their status)
python3 manage.py list <status>
e.g: python3 manage.py list
e.g: python3 manage.py list todo
e.g: python3 manage.py list done
e.g: python3 manage.py list in-progress
