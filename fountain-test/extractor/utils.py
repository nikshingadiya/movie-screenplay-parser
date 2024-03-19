import json
from typing import  List
def read_json(file_path):
    data = None
    with open(file_path, "r") as f:
        data = json.load(f)['tokens']
    return data

def write_json(filtered_data:List,output_file:str):
    with open(output_file, 'w') as outfile:
        json.dump(filtered_data, outfile)


