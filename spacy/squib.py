import spacy
from spacy import displacy

import xx_ent_wiki_sm
nlp = xx_ent_wiki_sm.load()

import glob
import os

dirname = os.path.dirname(__file__)
for input_path in glob.glob(os.path.join(dirname, '..', 'documents', '*.txt')):
  f = open(input_path, 'r')
  text = "\n".join(f.readlines())
  doc = nlp(text)
  #for ent in doc.ents:
  #    print(ent.text, ent.start_char, ent.end_char, ent.label_)
  #displacy.serve(doc, style='ent')
  html = displacy.render(doc, style='ent')
  basename = os.path.basename(input_path)
  outpath = os.path.join(dirname, basename.replace('.txt', '.html'))
  with open(outpath, 'w') as out:
    out.write(html)

