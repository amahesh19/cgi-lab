#!/usr/bin/env python3
import os, json, secret
from templates import login_page
print("Content-type:text/html\r\n\r\n")
print

#q1
# json_object = json.dumps(dict(os.environ), indent = 4)
# print(json_object)

# Q2
# if("QUERY_STRING" in os.environ.keys()):
#     print(os.environ["QUERY_STRING"])

#Q3
# if("HTTP_USER_AGENT" in os.environ.keys()):
#     print(os.environ["HTTP_USER_AGENT"])

#Q4
print(login_page())
