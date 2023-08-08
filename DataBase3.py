import sqlite3

class Database3:
    def __init__(self):
        self.con = sqlite3.connect('profile.db')
        self.cursor = self.con.cursor()
        self.create_profile_table() #create the tasks table

    def create_profile_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS profile(id integer PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT, grl TEXT, job TEXT, goal TEXT, law1 TEXT, law2 TEXT, law3 TEXT, law4 TEXT, law5 TEXT, law6 TEXT, law7 TEXT)")
        self.con.commit()

    def create_profile(self, name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7):
        """Create a task"""
        self.cursor.execute("INSERT INTO profile(name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7))
        self.con.commit()

    def get_profile(self):
        """Get all completed and uncomplete tasks"""
        profile = self.cursor.execute("SELECT name, title, grl, job, goal, law1, law2, law3, law4, law5, law6, law7 FROM profile").fetchall()
        # return the tasks to be added to the list when the application starts
        return profile

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE profile")