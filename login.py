#!/usr/bin/env python3
import cgi, cgitb, secret, time, os
from templates import secret_page

#Q5

# form  = cgi.FieldStorage()

# username = form.getvalue('username')
# password = form.getvalue('password')


# if(username == secret.username and password == secret.password):
#     print(f"Set-Cookie: username={username}\r\nSet-Cookie: password={password}\r\nContent-type:text/html\r\n\r\n")
#     print(secret_page(username, password))

#Q6
# if("HTTP_COOKIE" in os.environ.keys()):
#     cookie_list = os.environ["HTTP_COOKIE"].split(";")
#     username = ""
#     password = ""
#     for cookie in cookie_list:
#         if cookie.split("=")[0] == " username":
#             username = cookie.split("=")[1]
#         elif cookie.split("=")[0] == " password":
#             password = cookie.split("=")[1]
#     if(username == secret.username and password == secret.password):
#         print(secret_page(username, password))
