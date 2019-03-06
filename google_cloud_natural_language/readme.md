# Google Cloud Natural Language

Google Cloud Platform has a Named Entity Recognition (NER) API.  Their NER API is part of their natural language offerings alongside their Optical Character Recognition

## Installation & Usage

To use Google Cloud Natural Language APIs, you'll need to do a few things.

- Sign up for a Google Cloud Platform (GCP) account
- Create a project on GCP
- Add the Natural Language API to the project (as part of this you'll set up the right permissions)
- Download the credentials GCP provides you in a JSON file.

(Also see the instructions on how to get a project set up in our OCR post.)

Ted cribbed [Google's python sample](https://cloud.google.com/natural-language/docs/analyzing-entities#language-entities-string-python) for how to use the Natural Language API.  Ted also got annoyed that the API was consistently returning -1 for the position of all of the entities (which was due to the fact that [the API requires users to specify character encoding](https://stackoverflow.com/questions/52545026/begin-offset-is-set-to-1-google-natural-language-api-entity-extraction?rq=1)).

Ted validated that there was an issue w/ his usage by comparing against [Google Cloud's command line tool](https://cloud.google.com/natural-language/docs/quickstart).

```
brew tap caskroom/cask
brew cask install google-cloud-sdk
```

had to set `CLOUDSDK_PYTHON` in my environment.

```
export GOOGLE_APPLICATION_CREDENTIALS=google_cloud_natural_language/credentials.json 
gcloud ml language analyze-entities --content-file=./documents/new-republic-white-fish.txt > google_cloud_natural_language/new-republic-white-fish.json
```

## Outputs

Google Cloud Platform APIs return their results using the Protobuf format, and so users will be reliant on the Protobuf library for their programming language.  Most of these libraries have ways to turn these Protobuf objects into JSON.

Despite using google's official tools to read and analyze our files, Ted had trouble with google's output.

Google gives back a list of entities, and mentions of each entity, and where they show up in the text.  Unfortunately, the start and end positions of where the mentions appear are listed as the number of bytes from the beginning of the file, rather than the number of _characters_ from the beginning of the file.

This requires some rejiggering in order to correctly tabulate.

[Google's entity types][google_entity_types]

# Checklist

- Does it cost money?  Yes
    - how much?
- Is it open source?  No
- What kinds of entities does it identify? [They have a short list][google_entity_types]
- Does it require downloading model data? no
- Does it have a CLI? yes
- Can it be integrated into another program? yes
    - If so, what programming languages? A lot.  (go find a list)
- What kind of output do you get? It's all protobufs.
- How fast is it? Fast.
- Does it provide cross referencing of entities? Yes
    - between matches in the output? Yes
    - to wikipedia, or another knowledge base? Wikipedia & Knowledge Graph Ids.
- Qualitatively...
    - Did it miss entities?  A few?  A lot?
        - Even with relatively few types, GCP matches A LOT
    - Did it misclassify entities?
        - Yeah, although understandable things, like confusing references to "Whitefish" as the location rather than the energy company, or Maria as a person rather than the hurricane.  Although it also misclassified "Hurricane Maria" as a person.
        - It's overly aggressive.  It tags things that aren't relevant.

[google_entity_types]: https://cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type