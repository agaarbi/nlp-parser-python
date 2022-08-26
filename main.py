import entities

import json
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

# query = input('Enter your query: ')
query = "Putin and Imran Khan Met in Russia before the Ukranian War in february 2022"
print(query)

nlp_query = nlp(query)
query_ner = entities.Entities()

# named entity sorting in 5 groups (check docs for each label's descriptive name)
persons_labels = ['PERSON']
groups_labels = ['NORP']
locations_labels = ['FAC', 'ORG', 'GPE', 'LOC']
events_labels = ['EVENT']
time_references_labels = ['DATE', 'TIME']

for entry in nlp_query:
    if entry.ent_type_ in persons_labels:
        query_ner.persons = entry.text
    elif entry.ent_type_ in groups_labels:
        query_ner.groups = entry.text
    elif entry.ent_type_ in locations_labels:
        query_ner.locations = entry.text
    elif entry.ent_type_ in events_labels:
        query_ner.events = entry.text
    elif entry.ent_type_ in time_references_labels:
        query_ner.time_references = entry.text


# create json query in required format
# json dump is used to create json from the entity class
# other changes are made as per the requirement
json_str = json.dumps(query_ner.__dict__)

json_str = "{ \"Entities\": " + json_str + "}"
json_str = json_str.replace("_persons", "persons")
json_str = json_str.replace("_groups", "groups")
json_str = json_str.replace("_locations", "locations")
json_str = json_str.replace("_events", "events")
json_str = json_str.replace("_time_references", "time_references")

print(json_str)