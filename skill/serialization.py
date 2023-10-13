# Json
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Serialize and save to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# Deserialize from a file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)