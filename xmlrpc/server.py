import sqlite3
import sys
import uuid
from xmlrpc.server import SimpleXMLRPCServer

DATABASE_FILE_NAME = 'notes.s3db'
SQL_NOTE = {
    'create_table_if_not_exists': (
        "CREATE TABLE IF NOT EXISTS note ("
        "id VARCHAR(36) PRIMARY KEY, "
        "content TEXT);"
    ),
    'insert': "INSERT INTO note (id, content) VALUES (?, ?);",
    'select': "SELECT content FROM note WHERE id = ?;",
    'delete': "DELETE FROM note WHERE id = ?;",
}

HOST = 'localhost'
PORT = 8001


def main():
    conn = sqlite3.connect(DATABASE_FILE_NAME)
    cur = conn.cursor()
    cur.execute(SQL_NOTE['create_table_if_not_exists'])

    with SimpleXMLRPCServer((HOST, PORT), allow_none=True) as server:
        @server.register_function(name='create_note')
        def create_note(content):
            id_ = str(uuid.uuid4())
            cur.execute(SQL_NOTE['insert'], (id_, content))
            conn.commit()
            return id_

        @server.register_function(name='read_and_delete_note')
        def read_and_delete_note(id_):
            content = cur.execute(SQL_NOTE['select'], (id_,)).fetchone()
            if content:
                cur.execute(SQL_NOTE['delete'], (id_,))
                conn.commit()
                return content[0]

        print(f'Serving XML-RPC on {HOST} port {PORT}')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            conn.close()
            sys.exit()


if __name__ == '__main__':
    main()
