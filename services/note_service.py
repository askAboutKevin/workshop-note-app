# app/services/note_service.py
from data_access import note_data_access
from models.note import Note


def get_notes():
    return [Note(**note) for note in note_data_access.get_notes()]


def get_note_by_id(note_id):
    note = note_data_access.get_note_by_id(note_id)
    return Note(**note) if note else None


def create_note(note):
    note_data_access.create_note(note)


def update_note(note_id, note):
    note_data_access.update_note(note_id, note)


def delete_note(note_id):
    note_data_access.delete_note(note_id)
