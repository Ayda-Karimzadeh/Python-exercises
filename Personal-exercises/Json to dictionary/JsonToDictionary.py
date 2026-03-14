import json
from pprint import pprint

with open("company1.json","r") as f:
    # pprint(json.load(f))
    d = json.load(f)

pprint(d)