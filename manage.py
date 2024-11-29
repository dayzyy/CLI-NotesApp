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
delete_parser.add_argument('id', type=int, choices=CHOICES, help='Id of the note to delte')

update_parser = subparser.add_parser('update', help='Command for updating a note')
update_parser.add_argument('id', type=int, choices=CHOICES, help='Id of the note to update')
update_parser.add_argument('note', type=str,help='New contents of the note to update')

args = parser.parse_args()

print(args)

match args.command:
    case 'add':
        Note.objects.create(args.note)
    case 'delete':
        Note.objects.delete(args.id)
    case 'update':
        Note.objects.update(args.id, args.note)
