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
		# print(statement)
		self.cursor.execute(statement)
		queryset = self.cursor.fetchall()

		return queryset

	def getObject(self, table, condition=()):
		statement = f"select * from {table} where {condition[0]} = {condition[1]}"
		self.cursor.execute(statement)

		obj = dict(zip(self.cursor.column_names, self.cursor.fetchone()))
		return obj

	def getColumnFromStatement(self, statement):
		self.cursor.execute(statement)
		return self.cursor.column_names


	# def callProcedure(self, procName, arg):
	# 	# result_args = self.cursor.callproc(procName, args)
	# 	# self.cursor.callproc(procName, args)
	# 	# data = self.cursor.callproc(procName, args).fetchall()
	# 	statement 
	# 	self.cursor.execute(statement)
	# 	return data


# c = ConnectionToMySQl()
# print(c.cursor.execute("select * from cgtrinh"))
# print(c.cursor.column_names)

# conn = mysql.connector.connect(
# 			auth_plugin='mysql_native_password',
# 			database='project',
# 			user='root', 
# 			password='1',
# 			host='localhost',
# 		)

# cursor = conn.cursor()

# cursor.execute("call getKTSbyCtrinh(6);", multi=True)

# myresult = cursor.fetchall()


# for x in myresult:
# 	print(x)