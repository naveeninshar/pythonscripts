#!/usr/bin/python3

'''
IF ELSE IF WITH LIST
'''

user = [
    {'admin': False, 'active': False, 'name': 'John'},
    {'admin': True, 'active': False, 'name': 'Mark'},
    {'admin': False, 'active': True, 'name': 'Paul'},
    {'admin': True, 'active': True, 'name': 'Mike'}
]

for usr in user:
    if (usr['admin'] and usr['active']):
        print("ACTIVE - (ADMIN) {}".format(usr['name']))
    elif (usr['active']):
        print("ACTIVE {}".format(usr['name']))
    elif (usr['admin']):
        print("(ADMIN) {}".format(usr['name']))
    else:
        print("{}".format(usr['name']))
