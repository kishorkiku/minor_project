#!/usr/bin/python2
import cgi,os
import cgitb
cgitb.enable()
print "content-type:text/html"
print ""
#get the filename here
form=cgi.FieldStorage()
drive_name=form.getvalue('dn')
fileitem=form['filename']
#test if the file is present
if fileitem.filename:
#strip loading path from file name to avoid
#directory traversal attacks             
	    fn=os.path.basename(fileitem.filename.replace("\\","/"))
	    open("/var/www/html/CloudX/"+drive_name+"/" +fn,"wb").write(fileitem.file.read())
	    print 'The file "'+fn+ '"was uploaded successfully'
            print "<meta http-equiv='Refresh' content='1;url=http://192.168.122.55/CloudX/"+drive_name+"'/>"

else:
   print 'No file was uploaded'
