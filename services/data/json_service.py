import json


def write_json(filename, data):
    with open(filename, 'w') as f:
        print(type(data), data)
        result = {"results": data}
        f.write(json.dumps(result))

def read_json(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())