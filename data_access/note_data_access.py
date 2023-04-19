# app/data_access/note_data_access.py
import json

DATA_FILE = "notes.json"


def read_notes():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def write_notes(notes):
    with open(DATA_FILE, "w") as f:
        json.dump(notes, f, indent=4)


def get_notes():
    return read_notes()


def get_note_by_id(note_id):
    notes = read_notes()
    return next((note for note in notes if note["id"] == note_id), None)


def create_note(note):
    notes = read_notes()
    notes.append(vars(note))
    write_notes(notes)


def update_note(note_id, note):
    notes = read_notes()
    index = next((i for i, n in enumerate(notes) if n["id"] == note_id), None)
    if index is not None:
        notes[index] = vars(note)
        write_notes(notes)


def delete_note(note_id):
    notes = read_notes()
    notes = [note for note in notes if note["id"] != note_id]
    write_notes(notes)
