#!/usr/bin/python2
import cgi
import cgitb
cgitb.enable()
import commands
import mysql.connector as mariadb
print "content-type:text/html"
print ""

web_data=cgi.FieldStorage()
name=web_data.getvalue('name')
username=web_data.getvalue('username')
password=web_data.getvalue('password')
contect=web_data.getvalue('contect')
#creating connection with database
mariadb_connection=mariadb.connect(user='root',password='1234',database='clouduser',host='localhost')
cursor=mariadb_connection.cursor()
try:  
        cursor.execute('INSERT INTO clouduser (name,username,password,contect) VALUES(%s,%s,%s,%s)', (name,username,password,contect)) 
	mariadb_connection.commit()
	mariadb_connection.close()
	print "<meta http-equiv='refresh' content='0; url=http://127.0.0.1/index.html'>"
except:
 	print "<script>"
 	print "alert('check credential details')"
 	print "</script>"
 	print "<meta http-equiv='refresh' content='1; url=http://127.0.0.1/signup/signup.html'>"
