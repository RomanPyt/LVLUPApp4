import sqlite3

class Database5:
    def __init__(self):
        self.con = sqlite3.connect('data1.db')
        self.cursor = self.con.cursor()
        self.create_data_table() #create the tasks table

    def create_data_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data(id integer PRIMARY KEY AUTOINCREMENT, date INTEGER)")
        self.con.commit()

    def create_data(self, date):
        """Create a task"""
        self.cursor.execute("INSERT INTO data(date) VALUES(?)", (date,))
        self.con.commit()

    def get_data(self):
        """Get all completed and uncomplete tasks"""
        data = self.cursor.execute("SELECT id, date FROM data").fetchall()
        # return the tasks to be added to the list when the application starts
        return data

    def delete_date(self, taskid):
        """Delete a task"""
        self.cursor.execute("DELETE FROM data WHERE id=?", (taskid,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE data")