import os
import json

pcks_list = os.popen("pip list --outdated --format=json").read()
pcks_list = json.loads(pcks_list)

for pck_list in pcks_list:
    name = pck_list['name']

    cmd_out = os.popen(f"pip install {name} --upgrade").read()
    print(cmd_out)
