import json
from pathlib import Path
from app import create_app, db
from app.models import Anime, Manga

def clean_data(data):
    # Remove empty keys and clean the data
    return {k: v for k, v in data.items() if k and v is not None}

def populate_database():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.session.query(Anime).delete()
        db.session.query(Manga).delete()
        
        frontend_dir = Path(__file__).parent.parent / 'frontend' / 'public'
        
        # Load and insert anime data
        try:
            with open(frontend_dir / 'anime-response.json', 'r', encoding='utf-8') as f:
                anime_data = json.load(f)
                for entry in anime_data:
                    # Clean the data before creating the model
                    cleaned_entry = clean_data(entry)
                    anime = Anime(**cleaned_entry)
                    db.session.add(anime)
        except Exception as e:
            print(f"Error loading anime data: {e}")
            
        # Load and insert manga data
        try:
            with open(frontend_dir / 'manga-response.json', 'r', encoding='utf-8') as f:
                manga_data = json.load(f)
                for entry in manga_data:
                    # Clean the data before creating the model
                    cleaned_entry = clean_data(entry)
                    manga = Manga(**cleaned_entry)
                    db.session.add(manga)
        except Exception as e:
            print(f"Error loading manga data: {e}")
            
        db.session.commit()
        print("Database populated successfully!")

if __name__ == "__main__":
    populate_database() 