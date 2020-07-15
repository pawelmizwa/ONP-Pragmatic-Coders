import os
import operator

digits = set('0123456789')
operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
local_user = "candidate"
local_password = os.getenv("local_password", "change_me")
