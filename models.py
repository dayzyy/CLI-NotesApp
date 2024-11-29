from datetime import datetime
import json

class Status():
    ToDo = 'todo'
    InProgress = 'in-progress'
    Done = 'done'

class NoteManager():
    # Checks if database exists, if it doesnt it creates it.
    @classmethod
    def database(cls):
        try:
            with open('db.json', 'r'):
                pass
        except FileNotFoundError:
            with open('db.json', 'w') as database:
                json.dump({
                    "notes": [

                    ],
                    "instances": 0,
                }, database)

    # Returns a list of all the Note objects
    @classmethod
    def all(cls):
        with open('db.json', 'r') as database:
            notes = json.load(database)['notes']
            serializer = {
                'data': [],
            }
            for note in notes:
                serializer['data'].append(Note(note['id'], note['body'], note['status'], note['createdAt'] , note['updatedAt']))

            for note in serializer['data']:
                print(note)

    # Returns total amount of instances ever created (even if they have been deleted after)
    @classmethod
    def instance_count(cls):
        with open('db.json', 'r') as database:
            return json.load(database)['instances']

    # Saves a new note in the db.json
    @classmethod
    def create(cls, body):
        object = {
            'id': cls.instance_count() + 1,
            'body': body,
            'status': Status.ToDo,
            'createdAt': str(datetime.now()),
            'updatedAt': str(datetime.now()),
        }

        with open('db.json', 'r') as database:
            data = json.load(database)
            with open('db.json', 'w') as database:
                data['notes'].append(object)
                data['instances'] += 1
                json.dump(data, database)
        
class Note():
    objects = NoteManager

    def __init__(self, id, body, status, createdAt, updatedAt):
        self.id = id
        self.body = body
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __str__(self):
        return self.body

# Note.objects.create('First note of this project')
NoteManager.database()
print(Note.objects.all())
