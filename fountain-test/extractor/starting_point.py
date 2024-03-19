import re
import json
import argparse
from utils import read_json
def match_page_number(regex=r"page_number=\d+", text=None):
    return bool(re.match(regex, text))
    
def required_data_parse(data: dict, main_key="scene_heading") -> dict:
    starting_point = {"page_store": "0", "first_scene": None}
    for i in data:
        try:
            text = i['text']
            if i['type'] == "action" and match_page_number(text=text):
                starting_point['page_store'] = text
            elif i['type'] == main_key:
                starting_point['first_scene'] = text
                break
            
        except Exception as e:
            pass
    return starting_point



def screenplay_start(file_path):
    data = read_json(file_path)
    starting_dict = required_data_parse(data)
    print("starting_point",starting_dict)
    return starting_dict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process JSON file and extract required data.')
    parser.add_argument('--file', dest='file_path', type=str, required=True,
                        help='Path to the JSON file')

    args = parser.parse_args()
    file_path = args.file_path
    screenplay_start(file_path)
