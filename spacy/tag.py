import glob
import os
import sys
import json
import spacy
from spacy import displacy

model_size = sys.argv[1].lower()

if model_size == "small":
  model = 'en_core_web_sm'
elif model_size == "large":
  model = 'en_core_web_lg'
else:
  raise Exception("model size should be 'small' or 'large'")

nlp = spacy.load(model)

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
  jsonpath = os.path.join(dirname, basename.replace('.txt', f'.spacy.{model_size}.json'))
  with open(jsonpath, 'w') as jsonFile:
    json.dump({"entities": ents}, jsonFile)
  outpath = os.path.join(dirname, basename.replace('.txt', f'.spacy.{model_size}.html'))
  with open(outpath, 'w') as outFile:
    outFile.write(html)

