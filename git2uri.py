import json
from submission import Submission

teste = Submission("blabla", "24/02/1996", 3, "Java")
print(teste.code)
f = open("auths")
data = json.load(f)
print(data)
#print(data["github"]["user"])
#print(data["github"][0]["user"])
#print(data["github"][0]["password"])