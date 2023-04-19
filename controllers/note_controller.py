# app/controllers/note_controller.py
from flask import Blueprint, request, jsonify
from services import note_service
from models.note import Note

note_blueprint = Blueprint("note", __name__)


@note_blueprint.route("/notes", methods=["GET"])
def get_notes():
    notes = note_service.get_notes()
    return jsonify([vars(note) for note in notes])


@note_blueprint.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = note_service.get_note_by_id(note_id)
    if note:
        return jsonify(vars(note))
    else:
        return "Note not found", 404


@note_blueprint.route("/notes", methods=["POST"])
def create_note():

    # example error handling
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Bad request"}), 400

    data = request.get_json()
    note = Note(data["id"], data["title"], data["content"])
    note_service.create_note(note)
    return "Note created", 201


@note_blueprint.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.get_json()
    note = Note(note_id, data["title"], data["content"])
    note_service.update_note(note_id, note)
    return "Note updated", 200


@note_blueprint.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note_service.delete_note(note_id)
    return "Note deleted", 204
