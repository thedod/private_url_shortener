#!/usr/bin/env python
from getpass import getpass
from os import urandom
import hmac

confirmed = False
password_prompt = 'Password: '
while not confirmed:
    password = getpass(password_prompt)
    if password==getpass('Password (again): '):
        confirmed = True
    else:
        password_prompt = "Passwords don't match.\nPassword: "

password_salt = urandom(32)
password_hash = hmac.new(password_salt,password)

print '# Generated by {0}'.format(__file__)
print 'PASSWORD_SALT = {0}'.format(`password_salt.encode('hex')`)
print 'PASSWORD_HASH = {0}'.format(`password_hash.hexdigest()`)
