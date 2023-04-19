# app/controllers/note_controller.py
from flask import Blueprint, request, jsonify
from services import note_service
from models.note import Note

note_blueprint = Blueprint("note", __name__)


@note_blueprint.route("/notes", methods=["GET"])
def get_notes():
    notes = note_service.get_notes()
    return jsonify([vars(note) for note in notes])


# function get note by id


# function create note


# function update note

@note_blueprint.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note_service.delete_note(note_id)
    return "Note deleted", 204
