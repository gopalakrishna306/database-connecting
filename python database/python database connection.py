import pymysql
con=pymysql.connect(host="local",user="root",password="1234",db="mydb")

import mysql.connector
import mysql
con=mysql.connector.connect(host="localhost",user="root",password="1234",db="mydb")
curser=con.cursor()
curser.execute("show databases")
curser.execute("show tables")
print(curser.fetchall())
curser.execute("create database gopalakrishnapython")
curser.execute("show tables")
curser.fetchall()
curser.execute("use mydb")
curser.fetchall()
curser.execute('''insert into employes values (18,"python","compuert",23,173672)''')
curser.fetchall()
