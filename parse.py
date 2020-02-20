import os
import json
import hashlib

DATA_PATH = "./raw"
OUTPUT_PATH = "./subtitle"

def parse(filename):

    objects = []
    basename = os.path.basename(filename)
    programme = basename.split("_")[0]

    def clean(text):
        return text.replace("\n", "").replace("\u3000", " ")

    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    while len(lines) >= 3:
        id = clean(lines.pop(0))
        time = clean(lines.pop(0))
        text = clean(lines.pop(0))
        start_time, end_time = time.split(" --> ")
        object = {
            "id": id,
            "origin": basename,
            "programme": programme,
            "startTime": start_time,
            "endTime": end_time,
            "text": text,
        }
        objects.append(object)
        if lines:
            lines.pop(0)
    return objects


def parse_all_files():
    files = [os.path.join(DATA_PATH, file) for file in os.listdir(DATA_PATH)]
    objects = []
    for file in files:
        objects = objects + parse(file)
    return objects


def dump_output(object):
    json_str = json.dumps(object)
    sha1sum = hashlib.sha1(json_str.encode("utf-8")).hexdigest()
    with open(os.path.join(OUTPUT_PATH, "{}.json".format(sha1sum)), 'w') as f:
        f.write(json_str)


if __name__ == "__main__":
    objects = parse_all_files()
    for object in objects:
        print(object)
    for object in objects:
        dump_output(object)
