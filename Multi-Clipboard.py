import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"



def save_data(filepath, data):
    with open(filepath, "a") as f:
        json.dump(data, f)
        f.write("\n")

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = [json.load(line.strip()) for line in f if line.strip()]
            return data
    except:
        return{}
    

save_data("clipboard.json",{"key": "value"})


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved")
    elif command == "load":
        key =  input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist.")
            
    elif command == "list":
        print("LIST")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")