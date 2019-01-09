#!/usr/bin/python2
import cgi
import cgitb
cgitb.enable()
import commands
import mysql.connector as mariadb
print "content-type:text/html"
print ""

web_data=cgi.FieldStorage()
username=web_data.getvalue('username')
password=web_data.getvalue('pass')

#creating connection with database
mariadb_connection=mariadb.connect(user='root',password='1234',database='clouduser',host='localhost')
cursor=mariadb_connection.cursor()
cursor.execute('select username,password from clouduser where username=%s and password=%s',(username ,password))
out=cursor.fetchall()
mariadb_connection.close()
if len(out)>0:
 print "<meta http-equiv='Refresh' content='1;url=http://192.168.122.55/CloudX'/>"
else:
 print "<script>"
 print "alert('check credential details')"
 print "</script>"
 print "<meta http-equiv='refresh' content='1; url=http://127.0.0.1/'>"



