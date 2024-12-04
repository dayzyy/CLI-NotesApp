import argparse

from models import Task

Task.objects.database()

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
        Task.objects.create(args.note)
    case 'delete':
        if Task.objects.DoesNotExist(args.id):
            exit()
        Task.objects.delete(args.id)
    case 'update':
        if Task.objects.DoesNotExist(args.id):
            exit()
        Task.objects.update(args.id, args.note)
    case 'mark':
        if Task.objects.DoesNotExist(args.id):
            exit()
        match args.progress:
            case 'todo':
                Task.objects.mark_as(args.id, 'todo')
            case 'in-progress':
                Task.objects.mark_as(args.id, 'in-progress')
            case 'done':
                Task.objects.mark_as(args.id, 'done')
    case 'list':
        match args.criteria:
            case 'all':
                notes = Task.objects.all()
                Task.display(notes, status='all')
            case 'todo':
                notes = Task.objects.filter('todo')
                Task.display(notes)
            case 'in-progress':
                notes = Task.objects.filter('in-progress')
                Task.display(notes, status='in-progress')
            case 'done':
                notes = Task.objects.filter('done')
                Task.display(notes, status='done')
