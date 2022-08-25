# Python program to update
# JSON


import json

# JSON data:
x = '{ "organization":"GeeksForGeeks","city":"Noida","country":"India"}'
class d:
    def __init__(self , number) -> None:
        self.num = number
    def insert(self):
        z=json.loads(x)
        z.update({"number":self.num})
        print(json.dumps(z))

# python object to be appended
y = {"pin":110096}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))
x1=d("22")
x1.insert()
print(json.dumps(z))
