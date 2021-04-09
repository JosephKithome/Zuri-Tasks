import time, os, os.path, sqlite3

#Variables

##############SQLite3#################
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def SQLRegister(un, pw):
	cursor.execute("INSERT INTO accounts(username, password) VALUES('{}', '{}')".format(un, pw))
	conn.commit()
######################################
def login():
	cursor.execute("SELECT name, password FROM accounts")	

def register():
	username = input("Username: ")
	password = input("Password: ")
	confirm_password = input("Confirm Password: ")

	if not (password == confirm_password):
		print("Passwords do not match...")
		time.sleep(1)
		register();
	else:
		SQLRegister(username, password);
		print("Account Registered")
		login();

register()