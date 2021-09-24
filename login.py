#!/usr/bin/env python3
import cgi, cgitb, secret, time, os
from templates import secret_page

print("Content-type:text/html\r\n\r\n")
print

#Q5, Q6

# form  = cgi.FieldStorage()

# username = form.getvalue('username')
# password = form.getvalue('password')


# if(username == secret.username and password == secret.password):
#     print(f"<p>Set-Cookie: username={username} password={password}</p>")
#     print(secret_page(username, password))

#-----------------------------------------------------------------------#

#Q7
# if("HTTP_COOKIE" in os.environ.keys()):
#     cookie = os.environ["HTTP_COOKIE"]
#     username = cookie.split(";")[0].split("=")[1]
#     password = cookie.split(";")[1].split("=")[1]
#     if(username == secret.username and password == secret.password):
#         print(secret_page(username, password))