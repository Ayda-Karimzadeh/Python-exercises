import json
from pprint import pprint

with open("company1.json","r") as f:
    # pprint(json.loads(f))
    d = json.loads(f)

pprint(d)