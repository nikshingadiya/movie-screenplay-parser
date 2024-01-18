import json
import time
from scene_extractor import process_script
from extract_text_to_pdf import extract_text_from_pdf
from langchain_scene_parser import run_chat_chain
from tqdm import tqdm  # Import tqdm for progress tracking

def extract_data(file_path, stop_at=None, json_output_path="output.json"):
    try:
        whole_text = extract_text_from_pdf(file_path)
        script_result = process_script(whole_text)

        extracted_data_list = []
        for index, data in tqdm(enumerate(script_result, start=1), total=len(script_result), desc="Processing scenes"):
            scene_text = data[index]['scene_detail']['text']

            if len(scene_text) > 0:
                events_dict = run_chat_chain(scene_text)['scene_details']
                data[index]['scene_detail']['extracted_field'] = events_dict

            extracted_data_list.append(data)

            if stop_at and index == stop_at:
                break

        # Write the extracted data to a JSON file
        if len(extracted_data_list) > 0:
            with open(json_output_path, 'w') as json_file:
                json.dump(extracted_data_list, json_file, indent=2)

    except Exception as e:
        if len(extracted_data_list) > 0:
            with open(json_output_path, 'w') as json_file:
                json.dump(extracted_data_list, json_file, indent=2)
if __name__ == "__main__":
    # Specify the file path to your PDF
    pdf_file_path = "pacific-rim-2013_1.pdf"

    # Extract data, process script, run chat chain, and store in a JSON file up to the 4th index
    extract_data(pdf_file_path, stop_at=15)
