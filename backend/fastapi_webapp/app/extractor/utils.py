import json
from typing import  List

def start_scene():
    start_patch={
        "type": "scene_heading",
        "text": "INT. START - SCENE"
    }
    return start_patch

def read_json(file_path):
    data = None
    with open(file_path, "r") as f:
        data = json.load(f)['tokens']
    return data

def write_json(filtered_data:List,output_file:str):
    with open(output_file, 'w') as outfile:
        json.dump(filtered_data, outfile)


def organize_data(filtered_data):
    organize_dict = {}

    for i in filtered_data:
        if i['type'] == "scene_heading":
            current_key = i['text']
            organize_dict[current_key] = []
        else:
            organize_dict[current_key].append(i)
    print("scence_count",len(organize_dict.keys())-1)

    return organize_dict

# Example usage:
# Assuming filtered_data is the list of dictionaries containing your data
# organized_data = organize_data(filtered_data)
