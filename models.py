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
            return serializer['data']
    
    # Checks if Note with such id exists, if it does Returns True. If it doesnt it raises an error
    @classmethod
    def DoesNotExist(cls, id):
        notes = cls.all()

        for note in notes:
            if note.id == id: return False
        print(f'Value Error: No note with id: {id}!')
        return True
    
    # Returns all the notes that have status 'todo'
    @classmethod
    def filter(cls, status):
        with open('db.json', 'r') as database:
            notes = json.load(database)['notes']
            serializer = {
                'data': [],
            }
            for note in notes:
                if note['status'] == status:
                    serializer['data'].append(Note(note['id'], note['body'], note['status'], note['createdAt'] , note['updatedAt']))
            return serializer['data']


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

    # Deletes a note, with provided ID, from the database
    @classmethod
    def delete(cls, id):
        with open('db.json', 'r') as database:
            data = json.load(database)
            notes = data['notes']
            
            with open('db.json', 'w') as database:
                for note in notes:
                    if note['id'] == id:
                        data['notes'].remove(note)
                        json.dump(data, database)
    
    # Updates a note ,with the provied ID, in the database
    @classmethod
    def update(cls, id, body):
        with open('db.json', 'r') as database:
            data = json.load(database)
            notes = data['notes']
            
            with open('db.json', 'w') as database:
                for index, note in enumerate(notes):
                    if note['id'] == id:
                        data['notes'][index]['body'] = body
                        data['notes'][index]['updatedAt'] = str(datetime.now())
                        break
                json.dump(data, database)

    # Updates a note's status ,with the provied ID, in the database
    @classmethod
    def mark_as(cls, id, status):
        with open('db.json', 'r') as database:
            data = json.load(database)
            notes = data['notes']
            
            with open('db.json', 'w') as database:
                for index, note in enumerate(notes):
                    if note['id'] == id:
                        data['notes'][index]['status'] = status
                        data['notes'][index]['updatedAt'] = str(datetime.now())
                        break
                json.dump(data, database)
        
class Note():
    objects = NoteManager

    def __init__(self, id, body, status, createdAt, updatedAt):
        self.id = id
        self.body = body
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    @classmethod
    def display(cls, notes, status='todo'):
        match status:
            case Status.ToDo: print('******TO-DO******')
            case Status.InProgress: print('******IN-PROGRESS******')
            case Status.Done: print('******DONE******')
            case _: print('******ALL-TASKS******')

        print(f'{len(notes)} task{'' if len(notes) == 1 else 's'} in total', end='\n\n')
        for note in notes:
                print(f'--> {note} (id: {note.id} | status: {note.status})', end=f'{'\n' if note == notes[-1] else '\n\n'}')

    def __str__(self):
        return self.body
