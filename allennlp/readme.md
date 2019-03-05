# AllenNLP

- It's Pytorch based.
- It's FOSS
- It does a lot of things, including NER.
- It can be accessed programmatically, it also has a CLI.
- It has a lot of documentation, but some of it is out of date.

## Getting the CLI to work

- https://github.com/allenai/allennlp/blob/master/tutorials/getting_started/using_pretrained_models.md
- https://github.com/allenai/allennlp/issues/2276

output is only copypasta able from the CLI.

## Outputs

Okay so the predictor available for folks to use is built around the CoNLL-2003 data set (see [AllenNLP's model page](https://allennlp.org/models), and then click on "Named Entity Recognition" section).

CoNLL-2003 is not available publicly and a number of the links on [their page](https://www.clips.uantwerpen.be/conll2003/ner/) (which does not appear to have been updated since 2005) have gone dead.

A [complete list of joint annoations](https://www.clips.uantwerpen.be/conll2003/ner/etc/tags.eng) can be found here.

A guy named Max Hofer helpfully wrote up [a primer & glossary of annotations on text](https://towardsdatascience.com/deep-learning-for-ner-1-public-datasets-and-annotation-methods-8b1ad5e98caf) which explains what the AllenNLP tags mean.

They're broken down into two pieces separated by a hyphen.  The first piece indicates whether the current token is a single entity, outside of, inside of, the start of, or end of an entity.  This scheme is also [hidden away in SpaCy's documentation](https://spacy.io/usage/linguistic-features#updating-biluo).

