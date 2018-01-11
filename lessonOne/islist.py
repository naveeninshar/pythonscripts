#!/usr/bin/python3

'''
IF ELSE IF WITH LIST
'''

user = {'admin': False, 'active': False, 'name': 'John'}

if (user['admin'] and user['active']):
    print("ACTIVE - (ADMIN) {}".format(user['name']))
elif (user['active']):
    print("ACTIVE {}".format(user['name']))
elif (user['admin']):
    print("(ADMIN) {}".format(user['name']))
else:
    print("{}".format(user['name']))
