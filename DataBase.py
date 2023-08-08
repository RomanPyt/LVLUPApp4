import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('todo.db')
        self.cursor = self.con.cursor()
        self.create_task_table() #create the tasks table

    def create_task_table(self):
        """Create tasks table"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT NULL, value integer, completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)), day TEXT)")
        self.con.commit()

    def create_task(self, task, value=None, day='monday'):
        """Create a task"""
        self.cursor.execute("INSERT INTO tasks(task, value, completed, day) VALUES(?, ?, ?, ?)", (task, value, 0, day))
        self.con.commit()

        # GETTING THE LAST ENTERED ITEM SO WE CAN ADD IT TO THE TASK LIST
        created_task = self.cursor.execute("SELECT id, task, value FROM tasks WHERE task = ? and completed = 0", (task,)).fetchall()
        return created_task[-1]

    def get_tasks(self):
        """Get all completed and uncomplete tasks"""
        tasks = self.cursor.execute("SELECT id, task, value, day, completed FROM tasks").fetchall()
        # return the tasks to be added to the list when the application starts
        return tasks



    def mark_task_as_complete(self, taskid):
        """Mark tasks as complete"""
        self.cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (taskid,))
        self.con.commit()

    def mark_task_as_incomplete(self, taskid):
        """Mark task as uncomplete"""
        self.cursor.execute("UPDATE tasks SET completed=0 WHERE id=?", (taskid,))
        self.con.commit()

        # return the task text
        task_text = self.cursor.execute("SELECT task FROM tasks WHERE id=?", (taskid,)).fetchall()
        return task_text[0][0]

    def delete_task(self, taskid):
        """Delete a task"""
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (taskid,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def delete_db(self):
        self.cursor.execute("DROP TABLE tasks")