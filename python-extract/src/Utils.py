import json

def get_conf(file_conf):
     with open(file_conf) as file:
         conf = json.load(file)
     return conf