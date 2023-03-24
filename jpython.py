import json


jstring='{"subject":"cybersquare","grade":10}'
pyobj=json.loads(jstring)
print(jstring)
print(pyobj)
print(pyobj['subject'])

with open('sample.json','w') as f:
    json.dump(pyobj,f)
j1str=json.dumps(pyobj)
print(j1str)