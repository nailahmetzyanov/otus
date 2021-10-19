import json
from json import JSONEncoder

json_file = 'files/users.json'
result_json_file = 'files/result.json'


class User:
    name: str
    gender: str
    address: str
    age: str
    books: list

    def __init__(self, name, gender, address, age, **kwargs):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = []

    def __str__(self):
        return "User: name is %s, gender is %s, address is %s, age is %s, books: %s" % (
            self.name, self.gender, self.address, self.age, self.books)


def read_users(read_filename):
    with open(read_filename, 'r', encoding='utf-8') as file:
        users = []
        users_obj = json.load(file)
        for user in users_obj:
            users.append(User(**user))
        return users


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def encode_data(data):
    result = json.dumps(data, cls=MyEncoder)
    return result


def write_users(data, write_filename):
    data = json.dumps(data, cls=MyEncoder)
    data = json.loads(data)
    with open(write_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

