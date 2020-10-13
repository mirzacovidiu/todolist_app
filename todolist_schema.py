import sqlite3

connection = sqlite3.connect('todolist_schema.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(

	"""CREATE TABLE IF NOT EXISTS lists(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		title VARCHAR(32),
		content VARCHAR(32),
	);"""

	"""CREATE TABLE IF NOT EXISTS tasks(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		title VARCHAR(32),
		content VARCHAR(32),
	);"""
)
connection.commit()
cursor.close()
connection.close()
