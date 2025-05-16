import mysql.connector
#database connection
dataBase=mysql.connector.connect(
	host='localhost',
	user='root',
	password='Pra123'
	)
#prepare curssor object
cursorObject= dataBase.cursor()

#create database
cursorObject.execute('Create DATABASE ITD')
print("ALL Done")
