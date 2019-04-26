'''
To install spacy model use either of the following approaches:

Approach 1:
    pip install spacy
    python -m spacy download en_core_web_sm

Approach 2:
    pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz

'''

'''
To do:
    - Fix ending white space
    - Anonymize selective entity types
    - Option to replace with made up name in addition to place holders
    - Create stand-alone API
'''


import en_core_web_sm

def replace_name_with_placeholder(token):
    if token.ent_iob != 0 and token.ent_type_ == "PERSON":
        txt = "[REDACTED]"
    else:
        txt = token.text
    return txt + token.whitespace_

def anonymize_placeholder(text):
    nlp = en_core_web_sm.load()
    
    # parse the text with spacy
    doc = nlp(text)
    
    for ent in doc.ents:
        ent.merge()
    tokens = map(replace_name_with_placeholder, doc)
    return " ".join(tokens) 