books={}
books["bob"]={
    "name":"bob",
    "phone":8801529738723,
    "address":"bd"
}
books["alan"]={
    "name":"alan",
    "phone":8801629738723,
    "address":"dhaka"
}

import json
str=json.dumps(books)
with open("/media/frozen/Assistant/Document/Code/Repos/ML/Python/files/jsonFile.txt","w") as file:
    file.write(str)
