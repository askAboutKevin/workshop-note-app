# app/data_access/note_data_access.py
import json

DATA_FILE = "notes.json"

# example of a note
# {
#     "id": 1,
#     "title": "My first note",
#     "content": "This is my first note"
# }

# example of a list of notes
# [
#     {
#         "id": 1,
#         "title": "My first note",
#         "content": "This is my first note"
#     },
#     {
#         "id": 2,
#         "title": "My second note",
#         "content": "This is my second note"
#     }
# ]

### start helper functions to read and write notes ###
def read_notes():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def write_notes(notes):
    with open(DATA_FILE, "w") as f:
        json.dump(notes, f, indent=4)
### end helper functions to read and write notes ###


def get_notes():
    return read_notes()


# def get_note_by_id(note_id):

# def create_note(note):

# def update_note(note_id, note):

def delete_note(note_id):
    notes = read_notes()
    notes = [note for note in notes if note["id"] != note_id]
    write_notes(notes)
