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

def replace_name_with_placeholder(token, name_types=["PERSON"]):
    '''
    For a given token, return the token text or a place holder depending on the
    token type.
    Inputs:
        token: spaCy token object
        name_types: name types to be anonymized (default = "PERSON")
                    valid types include:
                        PERSON	People, including fictional.
                        NORP	Nationalities or religious or political groups.
                        FAC	Buildings, airports, highways, bridges, etc.
                        ORG	Companies, agencies, institutions, etc.
                        GPE	Countries, cities, states.
                        LOC	Non-GPE locations, mountain ranges, bodies of water.
                        PRODUCT	Objects, vehicles, foods, etc. (Not services.)
                        EVENT	Named hurricanes, battles, wars, sports events, etc.
                        WORK_OF_ART	Titles of books, songs, etc.
                        LAW	Named documents made into laws.
                        LANGUAGE	Any named language.
                        DATE	Absolute or relative dates or periods.
                        TIME	Times smaller than a day.
                        PERCENT	Percentage, including ”%“.
                        MONEY	Monetary values, including unit.
                        QUANTITY	Measurements, as of weight or distance.
                        ORDINAL	“first”, “second”, etc.
                        CARDINAL	Numerals that do not fall under another type.
    Outputs:
        text: either the origin token text or a place holder
    '''
    if token.ent_iob != 0 and token.ent_type_ in name_types:
        txt = "[REDACTED]"
    else:
        txt = token.text
    return txt + token.whitespace_


def anonymize_placeholder(text, name_types=["PERSON"]):
    '''
    Anonymize a piece of text by replacing names with a place holder.
    Inputs:
        text: input text
        name_types: name types to be anonymized (default = "PERSON")
                    valid types include:
                        PERSON	People, including fictional.
                        NORP	Nationalities or religious or political groups.
                        FAC	Buildings, airports, highways, bridges, etc.
                        ORG	Companies, agencies, institutions, etc.
                        GPE	Countries, cities, states.
                        LOC	Non-GPE locations, mountain ranges, bodies of water.
                        PRODUCT	Objects, vehicles, foods, etc. (Not services.)
                        EVENT	Named hurricanes, battles, wars, sports events, etc.
                        WORK_OF_ART	Titles of books, songs, etc.
                        LAW	Named documents made into laws.
                        LANGUAGE	Any named language.
                        DATE	Absolute or relative dates or periods.
                        TIME	Times smaller than a day.
                        PERCENT	Percentage, including ”%“.
                        MONEY	Monetary values, including unit.
                        QUANTITY	Measurements, as of weight or distance.
                        ORDINAL	“first”, “second”, etc.
                        CARDINAL	Numerals that do not fall under another type.
    Outputs:
        text: anonymized text
    '''
    nlp = en_core_web_sm.load()
    
    # parse the text with spacy
    doc = nlp(text)
    
    for ent in doc.ents:
        ent.merge()
    tokens = [replace_name_with_placeholder(t, name_types=name_types) for t in doc]
    return "".join(tokens) 