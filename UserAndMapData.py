import sqlite3


class User:
    def __int__(self):
        self.connection = sqlite3.connect('CRData')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS stats(
                            Cash INT,
                            Total_Cash INT
                            Time_Played INT,
                            Map_Complete INT,
                            Arrival_Complete INT,
                            Map_Open INT,
                            Car_Open INT,
                            Background_Open INT);""")
        q = self.cursor.execute("SEL * FROM stats").fetchall()
        if q is None:
            self.cursor.execute("INSERT INTO stats('Cash', 'Total_Cash', 'Time_Played', 'Map_Complete', "
                                "'Arrival_Complete', 'Map_Open', 'Car_Open', 'Background_Open') VALUES(?, ?, ?, ?, ?,"
                                " ?, ?, ?)", (0, 0, 0, 0, 0, 0, 1, 1))
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                            Car STR, 
                            Power REAL,
                            Clutch REAL,
                            Streamlining REAL,
                            Max_Speed REAL,
                            Price INT,
                            Structure STR);""")
        if self.cursor.execute("SEL * FROM cars").fetchall() is None:
            self.cursor.execute("INSERT INTO cars('Car', 'Power', 'Clutch', 'Streamlining', 'Max_Speed', 'Price',"
                                "'Structure') VALUES(?, ?, ?, ?, ?, ?, ?)", ('Lada', 1.0, 1.0, 1.0, 1.0, 0, 'lada0.png')
                                )
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS backgrounds(
                            Background STR,
                            Clutch REAL,
                            Price INT,
                            Structure STR);""")
        if self.cursor.execute("SEL * FROM backgrounds").fetchall() is None:
            self.cursor.execute("INSERT INTO backgrounds('Background', 'Clutch', 'Price', 'Structure') VALUES(?, ?, ?,"
                                "?)", ('Ice 1', 1.0, 0, 'Background1'))

    def get_car(self, name):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM cars WHERE Car = {name}").fetchall()

    def get_all_car(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM cars").fetchall()

    def get_background(self, background):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM backgrounds WHERE Background = {background}").fetchall()

    def get_all_background(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM backgrounds").fetchall()
