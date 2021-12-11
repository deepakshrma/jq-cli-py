import json
import sys
import re

key_to_parse = sys.argv[1]

reg = "(\.)|(\[(\d)\])"


def safeEval(key, obj):
    keys = re.findall(r"(\.(\w+))|(\[(\d+)\])", key)
    for (_, m1, __, m2) in keys:
        obj = obj[m1] if m1 in obj else None if m1 else obj[int(m2)]
        if obj == None:
            break
    return obj


def main():
    # Read JSON file
    json_file = open(sys.argv[2]) if len(sys.argv) > 2 else sys.stdin
    json_str = ""

    # Read JSON file line by line
    for line in json_file:
        json_str += line

    # Parse json string to dictionary
    json_dict = json.loads(json_str)

    ## Safe evaluate dictionary and parse.
    print(safeEval(key_to_parse, json_dict) or "")
