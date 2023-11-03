from flask import Flask
from flask import request
from datetime import datetime
import model
import logic


app = Flask(__name__)
_note_logic = logic.NoteLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_note: str) -> model.Note:
    parts = raw_note.split('|')

    if len(parts) != 3:
        raise ApiException(f"Invalid input format {raw_note}")

    input_data = 0

    try:
        input_data = int(datetime.strptime(parts[0], "%Y-%m-%d").timestamp())
        if input_data == 0:
            raise ApiException(f"Invalid input data format {parts[0]}")
    except Exception as ex:
        raise ApiException(f"Invalid input data {parts[0]}. {ex}")

    note = model.Note()
    note.id = None
    note.datatime = input_data
    note.title = parts[1]
    note.text = parts[2]

    return note


def _from_raw_update(raw_note: str) -> model.Note:
    parts = raw_note.split('|')

    if len(parts) != 2:
        raise ApiException(f"Invalid input format {raw_note}")

    note = model.Note()
    note.id = None
    note.datatime = 0
    note.title = parts[0]
    note.text = parts[1]
    return note


def _to_raw(note: model.Note) -> str:
    _data = datetime.fromtimestamp(note.datatime).strftime('%Y-%m-%d')
    return f"{_data}|{note.title}|{note.text}"


API_ROOT = "/api/v1"
NOTE_API_ROOT = API_ROOT + "/calendar"


@app.route(NOTE_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        note = _from_raw(data)
        _id = _note_logic.create(note)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(NOTE_API_ROOT + "/", methods=["GET"])
def list():
    try:
        notes = _note_logic.list()
        raw_notes = ""
        for note in notes:
            raw_notes += _to_raw(note) + '\r\n'
        return raw_notes, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(NOTE_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        note = _note_logic.read(_id)
        raw_note = _to_raw(note)
        return raw_note, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(NOTE_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        note = _from_raw_update(data)
        _note_logic.update(_id, note)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(NOTE_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _note_logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404


@app.route(NOTE_API_ROOT + "/", methods=["DELETE"])
def delete_all():
    try:
        _note_logic.delete_all()
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404
