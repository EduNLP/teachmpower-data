import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Initialize Firebase app
cred = credentials.Certificate("tmp-feedback-test-firebase-adminsdk-flei0-26191ff34a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_docname(index):
    docname = 'persuasive'
    if index > 0:
        docname = docname + str(index)
    return docname

def get_typename(index):
    return 'Persuasive Writing ' + str(index + 1)

hs_p = pd.read_csv('hs_persuasive_cta_sample.csv')
for index, row in hs_p.iterrows():
    doc_data = {
        'prompt': row['prompt'],
        'studentwork': row['essay'],
        'type': get_typename(index)
    }
    if index < 2:
        docname = get_docname(index)
        db.document('a2workshop_feedback/thinkaloud/hs1/' + docname).set(doc_data)
    else:
        docname = get_docname(index - 2)
        db.document('a2workshop_feedback/thinkaloud/hs2/' + docname).set(doc_data)

ms_p = pd.read_csv('ms_persuasive_cta_sample.csv')
for index, row in ms_p.iterrows():
    doc_data = {
        'prompt': row['prompt'],
        'studentwork': row['essay'],
        'type': get_typename(index)
    }
    if index < 2:
        docname = get_docname(index)
        db.document('a2workshop_feedback/thinkaloud/ms1/' + docname).set(doc_data)
    else:
        docname = get_docname(index - 2)
        db.document('a2workshop_feedback/thinkaloud/ms2/' + docname).set(doc_data)