import os
import json
from collections import Counter

SUBTITLE_PATH = "./subtitle"


def load_subtitles():
    subtitles = []
    subtitle_files = [os.path.join(SUBTITLE_PATH, x) for x in os.listdir(SUBTITLE_PATH)]
    for subtitle_file in subtitle_files:
        with open(subtitle_file, 'r') as f:
            subtitle = json.loads(f.read())
            subtitles.append(subtitle)
    return subtitles


def get_keywords_by_programme(entities, programme):
    programme_subtitles = filter(lambda x: x['programme'] == programme, subtitles)
    for subtitle in programme_subtitles:
        entities += subtitle['entities']
    filtered_entities = filter(lambda x: (x['type'] != 'NUMBER' and len(x['name']) > 1) and x['name'] != "人", entities)
    words = [entity['name'] for entity in filtered_entities]
    return words


if __name__ == "__main__":
    entities = []
    subtitles = load_subtitles()
    programme = "THKCCT2020M05301836"
    words = get_keywords_by_programme(entities, programme)
    print(words)
    counter = sorted([(k,v) for k, v in dict(Counter(words)).items()], key=lambda x: x[1], reverse=True)
    counter_list = []
    for name, count in counter:
        entity = {
            "name": name,
            "count": count,
        }
        counter_list.append(entity)
    print(counter_list)