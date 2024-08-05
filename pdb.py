import mysql.connector
def getConnection():
	global dbs
	global db1
	try:
		dbs = ["pdb1", "pdb2", "pdb3", "pdb4"]
		db1 = mysql.connector.connect(
			host="localhost",
			user="root",
			password="root"
		)	
	except:
		print("Error while trying to get a mysql connection")
	else:
		print("Connected to mysql successfully")
def getCursor():
	global c1
	try:
		c1 = db1.cursor()
	except:
		print("Error while trying to get a cursor")
	else:
		print("Successfully got a mysql cursor")
def createDatabases():
	try:
		for x in dbs:
			c1.execute("CREATE DATABASE "+x)
	except:
		print("Error while trying to create all required databases")
	else:
		print("Successfully created the required databases: pdb1, pdb2, pdb3, pdb4")
def performAllTasks():
	getConnection()
	getCursor()
	createDatabases()

performAllTasks()