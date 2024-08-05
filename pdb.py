import mysql.connector
def getMySQLConnection(host, user, password):
	global db1
	try:
		db1 = mysql.connector.connect(
			host=host,
			user=user,
			password=password
		)
	except:
		print("Error while trying to get a connection")
	else:
		print("Successfully got a mysql connection")
		
def getMySQLCursor():
	global c1
	try:
		c1 = db1.cursor()
	except:
		print("Error while trying to get a mysql cursor")
	else:
		print("Successfully got a mysql cursor")

def createMySQLdatabases(*dbs):
	try:
		for x in dbs:
			c1.execute("CREATE DATABASE "+x)
	except:
		print("Error while trying to create the required databases")
	else:
		print("Successfully created the required databases")

getMySQLConnection("localhost", "root", "root")
getMySQLCursor()
createMySQLdatabases("vik1", "vik2", "vik3", "vik4", "vik5")
