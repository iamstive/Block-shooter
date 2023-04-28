import sqlite3


class Map:
    def __init__(self):
        self.conn = sqlite3.connect("CRDBalph.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS map(
           type_obj INT,
           OX BIGINT,
           OY BIGINT,
           id BIGINT);""")
        print('poluchilis')

    def add_block(self, type_obj, OX, OY, id):
        with self.conn:
            return self.cursor.execute("INSERT INTO map('type_obj', 'OX', 'OY', 'id') VALUES(?, ?, ?, ?)", (type_obj, OX, OY, id))

    def out_all_blocks(self):
        with self.conn:
            return self.cursor.execute("SELECT * FROM map").fetchall()

    def delete_blocks(self):
        with self.conn:
            self.cursor.execute(F"DELETE FROM map WHERE type_obj = {1}")
            self.cursor.execute(f'DELETE FROM map WHERE type_obj = {2}')


class Maps:
    def __init__(self):
        self.connection = sqlite3.connect("CRDBalph.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                login TEXT,
                password TEXT,
                money TEXT,
                time_game TEXT);""")

    def add_map(self, name):
        return self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {name}(
        type_block INT,
        OX BIGINT,
        OY BIGINT)""")

    def add_block(self, name, type_obj, OX, OY):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {name}('type_obj', 'OX', 'OY') VALUES(?, ?, ?)", (type_obj, OX, OY))

    def out_all_blocks(self, name):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM {name}").fetchall()

    def delete_block(self, name, OX, OY):
        with self.connection:
            return self.cursor.execute(f"DELETE FROM {name} WHERE OX == {OX} && OY == {OY}")
