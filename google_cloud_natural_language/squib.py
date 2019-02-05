import google
import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.protobuf.json_format import MessageToJson

import glob
import os
import sys

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


dirname = os.path.dirname(__file__)
for input_path in glob.glob(os.path.join(dirname, '..', 'documents', '*.txt')):
    f = open(input_path, 'r')
    text = "\n".join(f.readlines())
    
    #text = 'President Kennedy spoke at the White House.'
    #text = '\n'.join(open('./documents/new-republic-white-fish.txt').readlines())

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    response = client.analyze_entities(document, encoding)
    print_entities(response.entities)
    basename = os.path.basename(input_path)
    outpath = os.path.join(dirname, basename.replace('.txt', '.json'))
    write_entity_json(response, outpath)
