# StanfordNLP

Regretfully, while StanfordNLP have released a PyTorch based [StanfordNLP python library](https://stanfordnlp.github.io/stanfordnlp/installation_download.html#quick-example) based around [CoNLL2018](https://universaldependencies.org/conll18/) which uses [the UniversalDependencies data](https://universaldependencies.org/), this does not appear to include NER tagging on the data set.  SpaCy for example suggests that [their NER pipeline can be mixed with the Stanford tools](https://github.com/explosion/spacy-stanfordnlp#experimental-mixing-and-matching-pipeline-components).

Instead we'll have to use [StanfordNLP's Java stack](https://nlp.stanford.edu/software/CRF-NER.shtml) and parse the results as text.

- [Corenlp.run](http://corenlp.run/)
- [Original Stanford NER demo site](http://nlp.stanford.edu:8080/ner/process)

# Checklist

- Does it cost money? No
- Is it open source? Yes
- What kinds of entities does it identify?
- Does it require downloading model data? No, they're bundled.
    - are there different prebuilt models? Yes, three different models.
- Does it have a CLI? Yes.
- Can it be integrated into another program?  Yes
    - If so, what programming languages?  Java.  There are also a vast number of libraries for different programming languages built to integrate w/ their self-hosted server APIs
- What kind of output do you get?  A text file with words and tags immediately after them.
- How fast is it?  It's pretty good.  Java is slow to start up.
- Does it provide cross referencing of entities? No
    - between matches in the output? No
    - to wikipedia, or another knowledge base? No
- Qualitatively...
    - Did it miss entities?  A few?  A lot?
    - Did it misclassify entities?
