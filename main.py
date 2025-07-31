import json
from firebase_config import init_firestore
from data_validation import is_duplicate

# Initialize Firestore
db = init_firestore()
collection_name = 'users'

# Load sample data
with open('sample_data.json', 'r') as file:
    entries = json.load(file)

# Fetch existing entries from Firestore
existing_entries = list(db.collection(collection_name).stream())

for entry in entries:
    if is_duplicate(entry, existing_entries):
        print(f"Duplicate Found: {entry}")
    else:
        db.collection(collection_name).add(entry)
        print(f"Added Unique Entry: {entry}")