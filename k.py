#!\Python27\python

print("Content-Type: text/html;charset=utf-8")
print("\r\n")
print("Hello World!\n")

import cgi

form=cgi.FieldStorage()


a_file=open("log.txt", "r+")

a_file.write(form.getvalue("name"))
a_file.close()