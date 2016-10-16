#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

class MySQLConnect(object):
	def __init__(self,host,user,pwd,db):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db

	def exectSQL(self,sql,flag):
		self.getConnect()
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			if flag:			#修改数据库
				self.closeConnect()
				return True
			else:				#查询数据库
				self.cursor.execute(sql)
				result = self.cursor.fetchall()
				self.closeConnect()
				return result
		except:
			self.conn.rollback()
			self.closeConnect()
			return False

	def getConnect(self):
		self.conn = MySQLdb.connect(self.host,self.user,self.pwd,self.db)
		self.cursor = self.conn.cursor()
		#print("connected")

	def closeConnect(self):
		self.cursor.close()
		self.conn.close()
		#print("closed")

if __name__ == "__main__":
	conn = MySQLConnect("localhost","root","root","test")

	version_sql="SELECT VERSION()"
	insert_sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Mac', 'Mohan', 20, 'M', 2000)
	select_sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

	result = conn.exectSQL(version_sql,False);print(result)
	result = conn.exectSQL(insert_sql,True);print(result)
	result = conn.exectSQL(select_sql,False)
	for row in result:
		fname = row[0];lname = row[1];age = row[2];sex = row[3];income = row[4]
		print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
