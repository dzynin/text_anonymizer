# Text.X
*Text.X* is a text anonymization app for journalists, newscasters, and content producers. It uses natural language processing to enable the users to anonymize different parts of a text (e.g., name of individuals, locations, dates, etc.). The app provides the option to replace the names (e.g., individuals, countries, organizations, etc.) with place holders or with fake names.

**Web app:** [https://text-anonymizer.herokuapp.com/](https://text-anonymizer.herokuapp.com/)

**Author:** [Aras Kayvanrad](https://www.linkedin.com/in/kayvanrad/).
**Company:** Insight Data Science, Toronto

It is common for journalists and content producers to anonymize stories or redact documents for privacy and/or security reasons. Depending on the content, various parts of the text may need to be anonymized/redacted. This may include name of individuals, locations, dates, monetary values, etc.

### Part-of-speech tagging
Text.x uses a [spaCy model](https://spacy.io/models) to parse and tag a document following tokenization.

![sample_pos.png](https://github.com/kayvanrad/text_anonymizer/blob/master/images/sample_pos.png)

Through the web app, the user selects the entity type(s) that she wishes to anonymize. Text.X currently supports the following entity types: 
- Person
- Nationalities or religious or political groups
- Companies, agencies, institutions, etc.
- Countries, cities, states
- Date
- Languages
- Monetary values 

Example: redact persons
```
The history of natural language processing generally started in the 1950s,
although work can be found from earlier periods. In 1950, [REDACTED] published
his famous article "Computing Machinery and Intelligence". In 1957,
[REDACTED] Syntactic Structures revolutionized Linguistics with
'universal grammar', a rule based system of syntactic structures.
[REDACTED] is widely considered to be the father of theoretical computer science.
```

### Anonymization with fictional names
It is often desired to replace names of individuals, places, languages, etc. with fictional names rather than with a place holder to maintain the integrity of the story. Text.X uses a list of fictional characters to anonymize stories with fictional names should the user wish to do so.

Example: replace individual names with fictional names
```
The history of natural language processing generally started in the 1950s,
although work can be found from earlier periods. In 1950, Fenchurch published
his famous article "Computing Machinery and Intelligence". In 1957,
Arthur Dent Syntactic Structures revolutionized Linguistics with
'universal grammar', a rule based system of syntactic structures.
Fenchurch is widely considered to be the father of theoretical computer science.
```

**Try Text.x** [text-anonymizer.herokuapp.com](https://text-anonymizer.herokuapp.com/)
