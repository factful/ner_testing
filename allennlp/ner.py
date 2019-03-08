import sys
import os
import json

import allennlp
from allennlp.predictors import Predictor

model_path = 'https://s3-us-west-2.amazonaws.com/allennlp/models/fine-grained-ner-model-elmo-2018.12.21.tar.gz'
predictor = Predictor.from_path(model_path)

input_path = sys.argv[1]
text = open(input_path).read()

results = predictor.predict(sentence=text)

# if you want the list of all of the possible labels
# check this out:
# list(predictor._model.vocab._token_to_index['labels'].keys())
#
# They're a combination of two lists:
# 
# Entity types:
# ["CARDINAL", "DATE", "EVENT", "FAC", "GPE", "LANGUAGE", "LAW", 
# "LOC", "MONEY", "NORP", "ORDINAL", "ORG", "PERCENT", "PERSON", 
# "PRODUCT", "QUANTITY", "TIME", "WORK_OF_ART"]
#
# And token position w/in the entity
# ["I", "U", "B", "L"]
#
# And lastly the tag could be "O" which means "outside" 
# of an entity.
#
# SpaCy has an explanation of the different entity types:
#   https://spacy.io/api/annotation#named-entities

# AllenNLP tokenizes the input and only provides token level
# position information.  So we have to glue it back together
# ourselves.  First we'll produce character offsets for each
# token.
token_offsets = []
position = 0
for word in results['words']:
    word_start = text.find(word, position)
    word_end = word_start + len(word)
    token_offsets.append((word_start,word_end))
    position = word_end

# Right now we have a bunch of parts that have to be filtered
# and composed into coherent data.
#
# First we'll filter out all of the tokens that aren't
# part of an entity.
entity_tokens = []
triples = zip(token_offsets, results['words'], results['tags'])
for positions, word, tag in triples:
  label = tag.split('-')[-1]
  if label != 'O':
    entity_tokens.append({
      'name': word,
      'start': positions[0],
      'end': positions[1],
      'tag': tag
    })

# Now that we have a list of all of the tokens which are
# part of an entity in `entity_tokens`, we can glom them
# together.
entities = []
token_iterator = iter(entity_tokens)
for token in token_iterator:
  #print("==========================")
  #print(token)
  token_position, label = token['tag'].split('-')
  # If the entity is only a single token it'll start with 'U'
  if token_position == 'U':
    entities.append({
      'name': token['name'],
      'type': label,
      'matches': [{
        'start': token['start'],
        'end': token['end'],
        'label': label
      }]
    })
  # if the entity is multiple tokens it'll start with 'B'
  # (B for Beginning!)
  elif token_position == 'B':
    # so, add the beginning token to a list of tokens
    tokens = [token]
    # and then keep grabbing tokens from the list
    # until we find a token that starts with 'L'
    # (L for Last!)
    while tokens[-1]['tag'][0] != 'L':
      tokens.append(next(token_iterator))

    #print("-------------------")
    #print("Tokens:")
    #print(tokens)

    # then slice the original text from the beginning
    # of the first token in the entity, to the end of 
    # the last token in the entity.
    entity_start = tokens[0]['start']
    entity_end = tokens[-1]['end']
    name = text[entity_start:entity_end]
    entities.append({
      'name': name,
      'type': label,
      'matches': [{
        'start': entity_start,
        'end':   entity_end,
        'label': label
      }]
    })
  else:
    # We should never get to this place!
    print("SOMETHING WENT WRONG!!!!")
    print("Not certain what to do with this token:")
    print(token)

dirname = "."
basename = os.path.basename(input_path)
jsonpath = os.path.join(dirname, basename.replace('.txt', '.allennlp.json'))
with open(jsonpath, 'w') as file:
  data = json.dumps({'entities': entities})
  file.write(data)
  print(data)
