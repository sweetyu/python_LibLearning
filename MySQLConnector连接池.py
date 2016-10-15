#!usr/bin/python
# coding=utf-8
import mysql.connector

user = 'root'
pwd  = 'root'
host = '127.0.0.1'
db   = 'test'

if __name__ == '__main__':
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cnx.close()