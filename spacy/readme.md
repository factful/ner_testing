# SpaCy

SpaCy is a recent Natural Language Processing (NLP) toolkit written in C and Python.  The choice of two languages is convenient so that users have the niceties of programming in Python, while all of the computationally hard parts of SpaCy can be fast, because they're written in C.

SpaCy was written with the explicit intent that developers could carry projects built on SpaCy into production with relative ease.

SpaCy has [excellent (and configurable) installation instructions](https://spacy.io/usage/).

[Downloading SpaCy models is similarly well documented](https://spacy.io/usage/models).

SpaCy doesn't really have a default output.  It's NER tools take [a document](https://spacy.io/api/doc) as a string and breaks it into [spans](https://spacy.io/api/span).  SpaCy does include [`displacy`](https://spacy.io/usage/visualizers), a visualization tool which can display data produced by SpaCy.

SpaCy lists [all of the entities](https://spacy.io/api/annotation#named-entities) tags they have (based on Ontonote), and an explanation of each tag.

## Interesting but not relevant

- [Break up of the founding SpaCy team](https://github.com/explosion/spaCy/issues/462)
- [SpaCy's announcement on Hacker News](https://news.ycombinator.com/item?id=8942783)
- [SpaCy's page at launch](https://web.archive.org/web/20150126012110/http://honnibal.github.io/spaCy/)
- [Explosion.ai's blog](https://explosion.ai/blog)
- [SpaCy benchmarks & stats](https://spacy.io/usage/facts-figures)