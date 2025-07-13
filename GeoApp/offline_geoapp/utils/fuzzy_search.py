
import difflib
import json
import os

def load_db(db_path):
    with open(db_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def fuzzy_lookup(address, db, limit=1):
    address = address.lower()
    matches = difflib.get_close_matches(address, db.keys(), n=limit, cutoff=0.6)
    if matches:
        best = matches[0]
        return best, db[best]
    return None, None
