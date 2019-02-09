import google
import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.protobuf.json_format import MessageToJson
from spacy import displacy

import glob
import os
import sys
import json

def print_entities(entities):
    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
        print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))

def write_entity_json(response, path):
    json_string = MessageToJson(response)
    with open(path, 'w') as out:
        out.write(json_string)

def htmlize(text_path, entity_path):
    # Read the text as binary because Google 
    with open(text_path, 'rb') as text_file:
        text = text_file.read()
        with open(entity_path) as entity_file:
            entity_data = json.load(entity_file)
            token_list = []
            for entity in entity_data['entities']:
                #print("========================")
                #derp = entity["name"]
                #ent_type = entity["type"]
                #token_count = len(entity['mentions'])
                #print(f"{derp} | {ent_type} | {token_count}")
                #print('------------------------')
                for mention in entity['mentions']:
                    start_position = mention['text']['beginOffset']
                    # Google returns start positions based on byte offsets, rather than
                    # character offsets.  So to calculate the _actual_ offset in the list of
                    # characters, we find the byte start position, read all of the characters
                    # up to that point and then ask python to recount the offset.
                    real_start = len(text[0:start_position].decode('utf-8'))
                    end_position = real_start + len(mention['text']['content'])
                    #print(f"Looking for: '{mention['text']['content']}' {start_position} | Found: '{text[start_position:end_position]}'")
                    token = {
                        'label': entity['type'], 
                        'start': real_start,
                        'end':   end_position
                    }
                    token_list.append(token)

            render_data = [{
                'text': text.decode('utf-8'),
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
    
    #text = 'President Kennedy spoke at the White House.'
    #text = '\n'.join(open('./documents/new-republic-white-fish.txt').readlines())

    client = language.LanguageServiceClient()

    #if isinstance(text, six.binary_type):
    #    text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF8
    #if sys.maxunicode == 65535:
    #    encoding = enums.EncodingType.UTF16

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    response = client.analyze_entities(document, encoding)
    print_entities(response.entities)
    basename = os.path.basename(text_path)
    json_path = os.path.join(dirname, basename.replace('.txt', '.json'))
    write_entity_json(response, json_path)
    htmlize(text_path, json_path)
