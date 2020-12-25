import mysql.connector


class ConnectionToMySQl():
	def __init__(self):
		self.connection = mysql.connector.connect(
			auth_plugin='mysql_native_password',
			database='project',
			user='root', 
			password='1',
			host='localhost',
		)
		self.cursor = self.connection.cursor()


	def getQueryset(self, statement):
		self.cursor.execute(statement)
		queryset = self.cursor.fetchall()

		return queryset

	def closeConnection(self):
		self.cursor.close()
		self.connection.close()