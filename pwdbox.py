import shelve
import sys

print('type add to add new password, and type search to search your account with password pasted, type del to delete '
      'your account and type exit to exit application')
pwds = []
pwdFile = shelve.open('pwdbox')
pwdKeys = pwdFile.keys()
if len(pwdKeys) > 0:
    pwds = pwdFile[pwdFile.keys()[0]]


def add(name, pwd):
    pwds.append({'name': name, 'pwd': pwd})
    print('save success.')

loop = True
try:
    while loop:
        print('please enter your account name')
        accountName = input()
        if accountName == '':
            continue
        elif accountName == 'exit':
            sys.exit(0)
        else:
            print('please enter your password')
            pwd = input()
            add(accountName, pwd)


except KeyboardInterrupt:
    loop = False
