#!/usr/bin/env python

import sys
import os
import json

import flair
from flair.data import Sentence
from flair.models import SequenceTagger

input_path = sys.argv[1]
text      = open(input_path).read()
sentence  = Sentence(text)
# This downloads a bunch of data by default.
# it'd be nice to be able to check if it's already installed
tagger    =  SequenceTagger.load('ner')
tagger.predict(sentence)

entities = []
for entity in sentence.get_spans('ner'):
  start = entity.start_pos
  end = entity.end_pos
  entities.append({
    'name': text[start:end],
    'type': entity.tag,
    'matches':[{
      'start': start,
      'end': end,
      'label': entity.tag}]
  })

#dirname = os.path.dirname(__file__)
dirname = "."
basename = os.path.basename(input_path)
jsonpath = os.path.join(dirname, basename.replace('.txt', '.flair.json'))
with open(jsonpath, 'w') as file:
  data = json.dumps({'entities': entities})
  file.write(data)
  print(data)
