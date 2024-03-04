import re

HEADING_ENUM = ["EXT./INT.", "EXT./INT.", "INT./EXT.", "EXT/INT", "INT/EXT", "INT.", "EXT.", "INT --", "EXT --"]

def is_heading(line):
    for heading in HEADING_ENUM:
        if not line.endswith(heading) and heading in line:
            return True
    return False

def extract_time_and_scene_data(text):
    time_vocab = "|".join([
        "NIGHT", "AFTERNOON", "MORNING", "DAYS", "DAY", "NIGHT", "DAYS", "DAY", "ANOTHER DAY", "LATER", "NIGHT",
        "SAME", "CONTINUOUS", "MOMENTS LATER", "LATER", "SUNSET",
    ])
    regex = '[-,]?[ ]?(DAWN|DUSK|((LATE|EARLY) )?' + time_vocab + ')|\d{4}'
    find_time = re.search(regex, text)

    txt = [x.strip("-,. ") for x in filter(None, text[find_time.end():].split())] if find_time else None
    scene_data = {
        "text": " ".join(txt) if txt else "",
    }
    return txt, scene_data

def extract_heading(text):
    region_match = re.search('((?:.* )?(?:EXT[\\.]?\\/INT[\\.]?|INT[\\.]?\\/EXT[\\.]?|INT(?:\\.| --)|EXT(?:\\.| --)))', text)
    region = region_match.groups()[0].strip() if region_match else ""
    time, scene_data = extract_time_and_scene_data(text)

    location = text.replace(region, "").strip()
    if time and len(time) > 0:
        location = location[:location.index(time[0])].rstrip()

    if len(region) > 0 and region[0].isdigit():
        region = region.lstrip('0123456789.- ')
        location = location.rstrip('0123456789.- ')

    time = time[:-1] if time and time[-1].isdigit() else time

    scene_info = {
        "region": region,
        "location": location,
        "text": " ".join(time) if time else "",
    }

    return scene_data, scene_info

def process_script(script_text):
    script_lines = script_text.split('\n')
    result = []
    current_data = {"text": ""}
    scene_counter = 1  # Initialize the scene counter

    for line in script_lines:
        if is_heading(line):
            if current_data["text"]:
                scene_detail, scene_info = extract_heading(current_data["text"])
                result.append({scene_counter: {'scene_info': scene_info, 'scene_detail': scene_detail}})
                current_data = {"text": ""}
                scene_counter += 1  # Increment the scene counter
            current_data["text"] += line
        else:
            current_data["text"] += " " + line

    # Handle the last block of text
    if current_data["text"]:
        scene_detail, scene_info = extract_heading(current_data["text"])
        result.append({scene_counter: {'scene_info': scene_info, 'scene_detail': scene_detail}})

    return result
