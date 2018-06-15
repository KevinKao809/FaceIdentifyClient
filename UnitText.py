# -*- coding: utf-8 -*-

import json
personText = '{"name":"Kevin Kao"}'

print(type(personText))

j = json.loads(personText)

print(type(j))

print(j['name'])
