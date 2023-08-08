import sqlite3

class Database2:
    def __init__(self):
        self.con = sqlite3.connect('quest.db')
        self.cursor = self.con.cursor()
        self.create_quest_table() #create the tasks table

    def create_quest_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS quests(id integer PRIMARY KEY AUTOINCREMENT, quest varchar(50) NOT NULL, value integer, date TEXT)")
        self.con.commit()

    def create_quest(self, quest, value=None, date=''):
        """Create a task"""
        self.cursor.execute("INSERT INTO quests(quest, value, date) VALUES(?, ?, ?)", (quest, value, date))
        self.con.commit()

        # GETTING THE LAST ENTERED ITEM SO WE CAN ADD IT TO THE TASK LIST
        created_task = self.cursor.execute("SELECT id, quest, value FROM quests WHERE quest = ?", (quest,)).fetchall()
        return created_task[-1]

    def get_quests(self):
        """Get all completed and uncomplete tasks"""
        quests = self.cursor.execute("SELECT id, quest, value, date FROM quests").fetchall()
        # return the tasks to be added to the list when the application starts
        return quests



    def delete_quest(self, taskid):
        """Delete a task"""
        self.cursor.execute("DELETE FROM quests WHERE id=?", (taskid,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE quests")