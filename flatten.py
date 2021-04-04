import json
import sys

def flattener(json_object):
    flattened = {}
    key_prefix = ""

    def flatten_json(json, key_prefix):
        if type(json) is dict:
            for x in json:
                flatten_json(json[x], key_prefix + x + ".")
        else:
            flattened[key_prefix[:-1]] = json


    flatten_json(json_object, key_prefix)
    return flattened


def main():
    try:
        json_filename = sys.argv[1]
        
        # opens .json input and converts to Python dict
        with open(json_filename, "r") as fp:
            json_input = json.load(fp)

        # flattened JSON as Python dict    
        flattened_json = flattener(json_input)

        # flattened JSON converted to JSON formatted str
        json_result = json.dumps(flattened_json, indent = 4)
        print(json_result)

        # converted flattened JSON (dict) to JSON formatted str and outputs to output.json
        with open("output.json", "w") as fp:
            json.dump(flattened_json, fp, indent = 4)
        
    except FileNotFoundError as e:
        print("Input file not valid. Errno:", e.errno)
    except IndexError as e:
        print("Most likely didn't input filename")



if __name__ == "__main__":
    main()


