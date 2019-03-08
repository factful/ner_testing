import json
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_lg')

import glob
import os

dirname = os.path.dirname(__file__)
for input_path in glob.glob(os.path.join(dirname, '..', 'documents', '*.txt')):
  text = open(input_path, 'r').read()
  doc = nlp(text)
  #for ent in doc.ents:
  #    print(ent.text, ent.start_char, ent.end_char, ent.label_)
  #displacy.serve(doc, style='ent')

  print("===============")
  ents = []
  for ent in doc.ents:
    entData = { 
      "name": ent.text, 
      "type": ent.label_, 
      "matches": [{
        "start":ent.start_char, 
        "end": ent.end_char, 
        "label":ent.label_}] 
    }
    print(entData)
    ents.append(entData)

  html = displacy.render(doc, style='ent')
  basename = os.path.basename(input_path)
  jsonpath = os.path.join(dirname, basename.replace('.txt', '.spacy.json'))
  with open(jsonpath, 'w') as jsonFile:
    json.dump({"entities": ents}, jsonFile)
  outpath = os.path.join(dirname, basename.replace('.txt', '.html'))
  with open(outpath, 'w') as outFile:
    outFile.write(html)

