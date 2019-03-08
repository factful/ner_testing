# AllenNLP

- It's Pytorch based.
- It's FOSS
- It does a lot of things, including NER.
- It can be accessed programmatically, it also has a CLI.
- It has a lot of documentation, but some of it is out of date.

AllenNLP's NER model is described thus:

> The named entity recognition model identifies named entities (people, locations, organizations, and miscellaneous) in the input text. This model is a reimplementation of the state-of-the-art NER model described in [Deep contextualized word representations](https://arxiv.org/abs/1802.05365), and uses a biLSTM with CRF layer and ELMo embeddings. It was trained on the CoNLL-2003 NER dataset, and has test set F1 of 92.5 for a single run, compared to the reported 92.22 +/- 0.10 F1 across five seeds in the reference paper.

So, breaking this description down... 

- It's a Deep Learning model (since AllenNLP uses PyTorch).
- It is a [biLSTM with a CRF layer](https://arxiv.org/abs/1508.01991)
    - a bidirectional Long Short-Term Memory (LSTM) is just a thing that can read a string of tokens and for any given token, make decisions about that token based on what tokens came before AND after that token.
    - a Conditional Random Field layer is 
- It uses [ELMo embeddings](https://allennlp.org/elmo).

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

# Checklist

- Does it cost money?  No
- Is it open source?  Yes
- What kinds of entities does it identify?  CoNNL entities.
- Does it require downloading model data? Yes
    - how large is the data? Big
    - are there different prebuilt models? No
- Does it have a CLI? No
- Can it be integrated into another program? Yes
    - If so, what programming languages? Python
- What kind of output do you get? A list of tokens & a list of tags
- How fast is it? It's slow.
- Does it provide cross referencing of entities? No
- Qualitatively...
    - Did it miss entities?  A few?  A lot?
        - It's pretty good!
        - it's the only one that correctly classified "Hurricane Maria" correctly.
        - 
    - Did it misclassify entities?
        - It's pretty good!
        - It still misclassifed "Maria"
