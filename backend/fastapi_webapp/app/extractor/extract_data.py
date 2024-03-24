import re
import json
import argparse
from starting_point import required_data_parse
from remove_duplicatepage import  remove_page_number
from  utils import read_json,write_json,start_scene,organize_data


def match_page_number(regex=r"page_number=\d+", text=None):
    return bool(re.match(regex, text))
    
def extract_data(data: dict, starting_point:dict) -> dict:
    start_page=starting_point["page_store"]
    extracted_data=[]
    flag=0
    for i in data:
        try:
            text = i['text']
            if i['type'] == "action" and start_page==text:
                starting_point['page_store'] = text
                flag=1
            elif flag==1 and not remove_page_number(text):
                extracted_data.append(i)
            else:
                pass    
        except Exception as e:
            pass
    return extracted_data



def screenplay_start(file_path, output_file):
    data = read_json(file_path)
    starting_dict = required_data_parse(data)
    print("Starting point:", starting_dict)
    filtered_data = extract_data(data, starting_dict)
    filtered_data.insert(0,start_scene())
    organize_dict=organize_data(filtered_data)
    
    write_json(organize_dict,output_file)
    print("Filtered data written to:", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process JSON file and extract required data.')
    parser.add_argument('--file', dest='file_path', type=str, required=True,
                        help='Path to the JSON file')
    parser.add_argument('--output', dest='output_file', type=str, required=True,
                        help='Path to the output JSON file')

    args = parser.parse_args()
    file_path = args.file_path
    output_file = args.output_file
    
    screenplay_start(file_path, output_file)
