import sqlite3

def show_color(username):
	connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(""" SELECT favorite_color FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
	color = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()
	message = 'Welcome {username}. Your favorite color is {color}.'.format(username=username, color=color)
	return message

def check_pw(username):
	connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(""" SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
	password = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()
	return password

def check_users():
	connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(""" SELECT username FROM users ORDER BY pk DESC;""")
	db_users = cursor.fetchall()
	users = []

	for i in range(len(db_users)):
		person = db_users[i][0]
		users.append(person)

	connection.commit()
	cursor.close()
	connection.close()

	return users

def signup(username, password, favorite_color):
	connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(""" SELECT password FROM users WHERE username = '{username}';""".format(username = username))
	exist = cursor.fetchone()

	if exist is None:
		cursor.execute("""INSERT INTO users(username, password, favorite_color)VALUES('{username}', '{password}', '{favorite_color}');""".format(username = username, password=password, favorite_color=favorite_color))
		connection.commit()
		cursor.close()
		connection.close()
	else:
		return ('User already existed!!')
	return 'You have successfuly signed up!!!'

def check_tasks(title, content):
	connection = sqlite3.connect('todolist-schema.db')
	cursor = connection.cursor()
	cursor.execute("""INSERT INTO tasks (title, content) VALUES ('{title}', '{content}');""".format(title = title, content = content))
