import csv
import json

def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as file:
            rows = list(csv.DictReader(file))
            with open("data.json") as file:
                json.dump(rows, file)
                return True
    except Exception:
        return False
