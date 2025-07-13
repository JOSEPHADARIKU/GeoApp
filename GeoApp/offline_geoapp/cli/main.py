import os
import sys

# 🔥 Add parent dir to sys.path so relative imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from offline_geoapp.utils.fuzzy_search import load_db, fuzzy_lookup

def main():
    print("📍 Offline GeoCoder (Fuzzy Edition)")
    db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'address_db.json')
    db_path = os.path.abspath(db_path)
    
    try:
        db = load_db(db_path)
    except FileNotFoundError:
        print("❌ address_db.json not found!")
        return

    while True:
        query = input("Enter address (or 'q' to quit): ").strip()
        if query.lower() == 'q':
            break
        match, result = fuzzy_lookup(query, db)
        if result:
            print(f"✅ Closest match: {match}")
            print(f"Latitude: {result['lat']}, Longitude: {result['lon']}")
        else:
            print("❌ No close match found.")

if __name__ == '__main__':
    main()
