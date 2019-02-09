from spacy import displacy
import glob
import os
import sys
import json

def htmlize(text_path, entity_path):
    with open(text_path) as text_file:
        text = text_file.read()
        with open(entity_path) as entity_file:
            entity_data = json.load(entity_file)
            entities = entity_data['documents'][0]['entities']
            token_list = []
            for entity in entities:
                ent_name = entity['name']
                ent_type = entity.get('type', "unk")
                token_count = len(entity['matches'])
                print("=======================")
                print(f"{ent_name} | {ent_type} | {token_count}")
                for match in entity['matches']:
                    start_position = match["offset"]
                    end_position = start_position + match["length"]
                    print("------------------------")
                    print(f"Looking for: \"{match['text']}\" {start_position} | Found: {text[start_position:end_position]}")
                    token = {
                        'label': ent_type,
                        'start': start_position,
                        'end': end_position
                    }
                    token_list.append(token)

            render_data = [{
                'text': text,
                'ents': token_list
            }]
            #print(render_data)
            html = displacy.render(render_data, style="ent", manual=True)
            html_path = os.path.join(entity_path.replace('.json', '.html'))
            with open(html_path, 'w') as out:
                out.write(html)


dirname = os.path.dirname(__file__)
for text_path in glob.glob(os.path.join(dirname, '..', 'documents', '*.txt')):
    f = open(text_path, 'r')
    text = f.read()
    basename = os.path.basename(text_path)
    json_path = os.path.join(dirname, basename.replace('.txt', '.json'))
    htmlize(text_path, json_path)
