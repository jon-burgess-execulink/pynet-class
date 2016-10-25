#!/usr/bin/env python

import yaml
import json

this_list = range(10)
this_list.append('hello')
this_list.append('world')
this_list.append({'name': 'this router', 'location': 'Toronto'})

with open("assignment1.yml", "w") as f:
    f.write(yaml.dump(this_list, default_flow_style=False))
    f.close()
    
with open("assignment1.json", "w") as f:
    json.dump(this_list, f)
    f.close()