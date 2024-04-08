file=open("/media/frozen/Assistant/Document/Code/Repos/ML/Python/files/jsonFile.txt")
str=file.read()

import json
data=json.loads(str)
print(data)
print(data["bob"])
print(data["bob"]["address"])
print("================")

for person in data:
    print(data[person])