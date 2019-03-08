# Azure Text Analytics

Azure's Cognitive Services has a Text Analytics API.

## Installation & Usage



## Outputs

[Azure organizes their tags][azure_entity_list] into a broad type and for some tags, into subtypes.

[azure_entity_list]: https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-entity-linking#supported-types-for-named-entity-recognition

# Checklist

- Does it cost money? Yes
- Is it open source? No
- What kinds of entities does it identify? [See the entity list][azure_entity_list]. It's based on CoNNL.
- Does it require downloading model data? (how large is the data?) No
- Does it have a CLI? No
- Can it be integrated into another program? Yes, it's an API
    - If so, what programming languages? 
        - Any language will work, you'll need to write an API wrapper.
- What kind of output do you get? JSON.
- How fast is it?  It's fast.
- Does it provide cross referencing of entities? Yes
    - between matches in the output? Yes
    - to wikipedia, or another knowledge base? Yep, Wikipedia.
- Qualitatively...
    - Did it miss entities?  A few?  A lot?
        - Azure provides more entity types & subtypes than any of the other tools.
    - Did it misclassify entities?
        - Yes.  Hurricane Maria is listed as a person.
        - It didn't know what to do with "Whitefish" or "Whitefish Energy".
        - It also misclassified "Trump Victory PAC" as a person named "Trump Victory" and an unkonwn entity "PAC"
