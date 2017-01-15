import json
import os.path as path

def load_data(filepath):
    if path.exists(filepath):
        with open(filepath) as file:
            return json.load(file)
    else:
        return None


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    while True:
        print("Enter your filepath:")
        jsonpath = input()
        if jsonpath != None:
            jsondata = load_data(jsonpath)
            if jsondata:
                pretty_print_json(jsondata)
                break
