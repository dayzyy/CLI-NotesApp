import argparse

from models import Note

Note.objects.database()

CHOICES = []
for id in range(Note.objects.instance_count()):
    CHOICES.append(id + 1)

parser = argparse.ArgumentParser(description='Manage your notes')

subparser = parser.add_subparsers(dest='command', help='Commands')

add_parser = subparser.add_parser('add', help='Command for creating a new note')
add_parser.add_argument('note', help='Note to add')

delete_parser = subparser.add_parser('delete', help='Command for deleting a note')
delete_parser.add_argument('id', type=int, help='Id of the note to delte')

update_parser = subparser.add_parser('update', help='Command for updating a note')
update_parser.add_argument('id', type=int, help='Id of the note to update')
update_parser.add_argument('note', type=str,help='New contents of the note to update')

list_parser = subparser.add_parser('list', help='Command to list all notes')
list_parser.add_argument('criteria', choices=['todo', 'in-progress', 'done', 'all'], help='Criteria to filter out the notes', nargs='?', default='all')

mark_parser = subparser.add_parser('mark', help='Command to change status of a note')
mark_parser.add_argument('id', type=int, help='Id of the note to change the status of')
mark_parser.add_argument('progress', choices=['todo', 'in-progress', 'done'], help='The status to set for the given note')

args = parser.parse_args()

match args.command:
    case 'add':
        Note.objects.create(args.note)
    case 'delete':
        if Note.objects.DoesNotExist(args.id):
            exit()
        Note.objects.delete(args.id)
    case 'update':
        if Note.objects.DoesNotExist(args.id):
            exit()
        Note.objects.update(args.id, args.note)
    case 'mark':
        if Note.objects.DoesNotExist(args.id):
            exit()
        match args.progress:
            case 'todo':
                Note.objects.mark_as(args.id, 'todo')
            case 'in-progress':
                Note.objects.mark_as(args.id, 'in-progress')
            case 'done':
                Note.objects.mark_as(args.id, 'done')
    case 'list':
        match args.criteria:
            case 'all':
                notes = Note.objects.all()
                Note.display(notes, status='all')
            case 'todo':
                notes = Note.objects.filter('todo')
                Note.display(notes)
            case 'in-progress':
                notes = Note.objects.filter('in-progress')
                Note.display(notes, status='in-progress')
            case 'done':
                notes = Note.objects.filter('done')
                Note.display(notes, status='done')

