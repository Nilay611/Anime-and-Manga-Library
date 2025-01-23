from . import db
from datetime import datetime

class Anime(db.Model):
    __tablename__ = 'anime'
    
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255))
    Type = db.Column(db.String(50))
    Episodes = db.Column(db.Integer)
    Aired = db.Column(db.String(100))
    Members = db.Column(db.Integer)
    Score = db.Column(db.Float)
    Rank = db.Column(db.Integer)
    image_url = db.Column(db.String(500))
    page_url = db.Column(db.String(500))

    def to_dict(self):
        return {
            'id': self.id,
            'Title': self.Title,
            'Type': self.Type,
            'Episodes': self.Episodes,
            'Aired': self.Aired,
            'Members': self.Members,
            'Score': self.Score,
            'Rank': self.Rank,
            'image_url': self.image_url,
            'page_url': self.page_url
        }

class Manga(db.Model):
    __tablename__ = 'manga'
    
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255))
    Type = db.Column(db.String(50))
    Volumes = db.Column(db.Integer)
    Published = db.Column(db.String(100))
    Members = db.Column(db.Integer)
    Score = db.Column(db.Float)
    Rank = db.Column(db.Integer)
    image_url = db.Column(db.String(500))
    page_url = db.Column(db.String(500))

    def to_dict(self):
        return {
            'id': self.id,
            'Title': self.Title,
            'Type': self.Type,
            'Volumes': self.Volumes,
            'Published': self.Published,
            'Members': self.Members,
            'Score': self.Score,
            'Rank': self.Rank,
            'image_url': self.image_url,
            'page_url': self.page_url
        }

class SavedAnime(db.Model):
    __tablename__ = 'saved_anime'
    
    id = db.Column(db.Integer, primary_key=True)
    anime_id = db.Column(db.Integer, db.ForeignKey('anime.id'))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Plan to Watch')  # Plan to Watch, Watching, Completed
    
    def to_dict(self):
        return {
            'id': self.id,
            'anime_id': self.anime_id,
            'date_added': self.date_added.isoformat(),
            'status': self.status
        }

class SavedManga(db.Model):
    __tablename__ = 'saved_manga'
    
    id = db.Column(db.Integer, primary_key=True)
    manga_id = db.Column(db.Integer, db.ForeignKey('manga.id'))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Plan to Read')  # Plan to Read, Reading, Completed
    
    def to_dict(self):
        return {
            'id': self.id,
            'manga_id': self.manga_id,
            'date_added': self.date_added.isoformat(),
            'status': self.status
        }
