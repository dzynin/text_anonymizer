# This script runs a text anonymizer on a sample text and
# produces a few illustrations

import en_core_web_sm
import text_anonymizer

text = """
The history of natural language processing generally started in the 1950s,
although work can be found from earlier periods. In 1950, Alan Turing published
his famous article "Computing Machinery and Intelligence". In 1957,
Noam Chomsky’s Syntactic Structures revolutionized Linguistics with
'universal grammar', a rule based system of syntactic structures.
Alan Turing is widely considered to be the father of theoretical computer science.
"""

print(text)

print(text_anonymizer.anonymize(text,name_types=["PERSON"], fictional=False))

print(text_anonymizer.anonymize(text,name_types=["PERSON"], fictional=True))

from spacy import displacy

nlp = en_core_web_sm.load()
doc = nlp(text)
displacy.serve(doc, style="ent")