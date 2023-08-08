import sqlite3

class Database4:
    def __init__(self):
        self.con = sqlite3.connect('level.db')
        self.cursor = self.con.cursor()
        self.create_level_table() #create the tasks table

    def create_level_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS level(lvl TEXT DEFAULT 1, value INTEGER DEFAULT 0, max INTEGER DEFAULT 1000)")
        self.con.commit()

    def create_level(self, lvl, value, max):
        """Create a task"""
        self.cursor.execute("INSERT INTO level(lvl, value, max) VALUES(?, ?, ?)", (lvl, value, max))
        self.con.commit()

    def get_lvl(self):
        """Get all completed and uncomplete tasks"""
        profile = self.cursor.execute("SELECT lvl, value, max FROM level").fetchall()
        # return the tasks to be added to the list when the application starts
        return profile

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE level")