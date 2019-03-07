# ner_testing

## Tools that we've tested

- SpaCy
- AllenNLP
- Google Cloud Natural Language
- Azure Entity Service
- Flair

## Tools we've yet to test

- [Stanford CoreNLP](https://github.com/explosion/spacy-stanfordnlp)
- Lightner
- [DBPedia Spotlight](https://www.dbpedia-spotlight.org/)
- 

## Tools we tried to test

[OpeNER](http://www.opener-project.eu/getting-started/) seemed promising, as it breaks things down into components and is open source.  Unfortunately their project doesn't look like it's been updated in a couple of years, and their entity recognizer doesn't work.

## Questions of interest

- Does it cost money?
- Is it open source?
- What kinds of entities does it identify?
- Does it require downloading model data? (how large is the data?)
    - are there different prebuilt models?
- Does it have a CLI?
- Can it be integrated into another program?
    - If so, what programming languages?
- What kind of output do you get?
- How fast is it?
- Does it provide cross referencing of entities?
    - between matches in the output?
    - to wikipedia, or another knowledge base?
- Qualitatively...
    - Did it miss entities?  A few?  A lot?
    - Did it misclassify entities?

## Broader questions

- What do these tools _do_ functionally?
    - Find entities 
- What do these tools do _technically_?
- How do these tools differ under the hood?
- How does entity extraction relate to other tools?
    - Well NER is a sequence labeling task.  There are other sequence labelers, some of which get used in the news, like many of the products which DataMade has built & deployed.
    - There are other approaches to information extraction.