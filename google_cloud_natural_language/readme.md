# Google Cloud Natural Language

Google Cloud Platform has a Name Entity Recognition API.  

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