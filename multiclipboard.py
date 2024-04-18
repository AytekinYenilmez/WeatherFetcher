import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file)

def load_items(filepath):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except:
        return {}



if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key not found!")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command!")