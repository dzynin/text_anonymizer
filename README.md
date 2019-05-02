# Text Anonymizer
*Text Anonymizer* is a text anonymization app for journalists, newscasters, and content producers. It uses natural language processing to enable the users to anonymize different parts of a text (e.g., name of individuals, locations, dates, etc.). The app provides the option to replace the names (e.g., individuals, countries, organizations, etc.) with place holders or with fake names.

**Web app:** [https://text-anonymizer.herokuapp.com/](https://text-anonymizer.herokuapp.com/)

**Author:** [Aras Kayvanrad](https://www.linkedin.com/in/kayvanrad/).
**Company:** Insight Data Science, Toronto

It is common for journalists and content producers to anonymize stories or redact documents for privacy and/or security reasons. Depending on the content, various parts of the text may need to be anonymized/redacted. This may include name of individuals, locations, dates, monetary values, etc.

Through the web app, the user selects the entity type(s) that she wishes to anonymize. Text Anonymizer currently supports the following entity types: 
- Person
- Nationalities or religious or political groups
- Companies, agencies, institutions, etc.
- Countries, cities, states
- Date
- Languages
- Monetary values 

The app provides the option to to redact the text by replacing these entities with a place holder or to replace them with fictional names, as it is often desired to replace names of individuals, places, languages, etc. with fictional names rather than with a place holder to maintain the integrity of the story. Text Anonymizer uses a list of fictional characters to anonymize stories with fictional names should the user wish to do so.

Example: redact persons
```
[REDACTED] was an American inventor and businessman. [REDACTED] was born
in 1847 in Milan, Ohio. [REDACTED] was on hand to turn on the lights at the
Hotel Edison in New York City when it opened in 1931.

[REDACTED] served as the third president of the United States
from 1801 to 1809. [REDACTED] was born on April 13, 1743.
```

Example: replace individual names with fictional names
```
Humma Kavula was an American inventor and businessman. Humma was born
in 1847 in Milan, Ohio. Kavula was on hand to turn on the lights at the
Hotel Edison in New York City when it opened in 1931.

Trillian Astra served as the third president of the United States
from 1801 to 1809. Trillian was born on April 13, 1743.
```

### Natural language processing (NLP)
Text Anonymizer uses the [English core web spaCy model](https://spacy.io/models) to parse and tag a document following tokenization.

![sample_pos.png](https://github.com/kayvanrad/text_anonymizer/blob/master/images/sample_pos.png)

In addition to the generic NLP processing, Text Anonymizer performs further processing, specifically for anonymization with fictional names. Some of the spefic processing is demonstrated by the above example, as follows:

Thomas Edison is referred to by first name (Thomas) and last name (Edison). Once an entity is identified as a PERSON, Text Anonymizer tries to identify the person, and the fictional person assigned to them - or assign a fictional person if the person is seen for the first time. Text Anonymizer then identifies whether the person was called by full name or first / last name, and matches the reference to the ficitonal person accordingly. In the above example, Thomas Edison is given the fictional name Humma Kavula. Reference to Thomas are replaced with Humma and references to Edison are replaced by Kavula.

Moreover, if there are people in the text with the same first or last name, Text Anonymizer attempts to identify which person was referred to based on the text preceeding the reference. In the above example, Thomas Edison and Thomas Jefferson share the same first name. If called by first name, Text Anonymizer attempts to identify the person based on the preceeding text.

### Further development
Text Anonymizer currently does not match gender for fictional names. To use gender specific fictional names, further development will require to identify the gender of the characters referred to in the text. This can be done, for example, based on the associated pronouns.

It may also be desired to anonymize the gender, which will require not only use of gender-neutral fictional names, but also replacing the associated pronouns with gender-neutral pronouns.


**Try Text Anonymizer** [text-anonymizer.herokuapp.com](https://text-anonymizer.herokuapp.com/)
