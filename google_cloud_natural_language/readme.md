# Google Cloud Natural Language

Google Cloud Platform has a Name Entity Recognition API.  



It's a lot simpler to install [google's sdk](https://cloud.google.com/natural-language/docs/quickstart).

```
brew tap caskroom/cask
brew cask install google-cloud-sdk
```

had to set `CLOUDSDK_PYTHON` in my environment.

```
export GOOGLE_APPLICATION_CREDENTIALS=google_cloud_natural_language/credentials.json 
gcloud ml language analyze-entities --content-file=./documents/new-republic-white-fish.txt > google_cloud_natural_language/new-republic-white-fish.json
```
