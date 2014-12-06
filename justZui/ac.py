#!/usr/bin/python

import json

jsonStr = '{"script":"123"}'

j = json.loads(jsonStr)
print j
shell_script = j['script']
print shell_script