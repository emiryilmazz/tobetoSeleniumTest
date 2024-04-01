import json
from pprint import pprint

veri = {}
veri ["test_invalid_login"] = {
    "username": "bir",
    "password": "bir",
    }

veri ["test_user_locked"] = {
    "username": "locked_out_user",
    "password": "secret_sauce",
}

veri ["test_valid_login"] = {
    "username": "standard_user",
    "password": "secret_sauce",
}

veriler = json.dumps(veri)
with open("veri.json","w") as w:
    w.write(veriler)

with open("veri.json","r") as r:
    oku = r.read()

pprint(json.loads(oku))