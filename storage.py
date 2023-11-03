from typing import List
import sqlite3
import time
from datetime import datetime
import model

db_connection = sqlite3.connect('database.db', check_same_thread=False)
db_cursor = db_connection.cursor()

db_cursor.execute('''
CREATE TABLE IF NOT EXISTS Calendar (
id INTEGER PRIMARY KEY,
datatime INTEGER NOT NULL,
title TEXT NOT NULL,
text TEXT NOT NULL
)''')
db_connection.commit()


class StorageException(Exception):
    pass


class LocalStorage:

    def create(self, note: model.Note) -> int:

        query = f'SELECT * FROM Calendar WHERE datatime = {note.datatime}'
        db_cursor.execute(query)
        notes = db_cursor.fetchall()

        if len(notes) != 0:
            raise StorageException("There is already a recording "
                                   "for this day!")

        #cur_data = datetime.fromtimestamp(int(note.datatime)). \
        #    strftime('%Y-%m-%d %H:%M:%S')
        #print(f'added data:{cur_data}')

        db_cursor.execute('INSERT INTO Calendar (datatime, title, text)'
                          ' VALUES (?, ?, ?)',
                          (int(note.datatime), note.title, note.text))

        db_connection.commit()

        db_cursor.execute('SELECT last_insert_rowid();')
        new_id = db_cursor.fetchall()

        return new_id[0][0]

    def list(self) -> List[model.Note]:
        db_cursor.execute('SELECT * FROM Calendar')
        notes = db_cursor.fetchall()

        result = []
        for row in notes:
            note = model.Note()
            note.id = row[0]
            note.datatime = row[1]
            note.title = row[2]
            note.text = row[3]
            result.append(note)
        return list(result)

    def read(self, _id: str) -> model.Note:

        db_cursor.execute('SELECT * FROM Calendar WHERE id = ?', (_id))
        notes = db_cursor.fetchall()

        if len(notes) != 1:
            raise StorageException(f"{_id} not found in db")

        for row in notes:
            result = model.Note()
            result.id = row[0]
            result.datatime = row[1]
            result.title = row[2]
            result.text = row[3]
            return result

    def update(self, _id: str, note: model.Note):

        db_cursor.execute('UPDATE Calendar SET title = ?, text = ?'
                          '  WHERE id = ?',
                          (note.title, note.text, _id))
        db_connection.commit()

        affected_rows = db_cursor.rowcount

        if affected_rows is not None and affected_rows > 0:
            # Update was successful, take appropriate action
            pass
        else:
            raise StorageException(f"{_id} not found in db")

    def delete(self, _id: str):

        db_cursor.execute('DELETE FROM Calendar WHERE id = ?', (_id))
        db_connection.commit()

        affected_rows = db_cursor.rowcount

        if affected_rows is not None and affected_rows > 0:
            # Update was successful, take appropriate action
            pass
        else:
            raise StorageException(f"{_id} not found in db")

    def delete_all(self):
        db_cursor.execute('DELETE FROM Calendar')
        db_connection.commit()
        pass
