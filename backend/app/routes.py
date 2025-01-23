from flask import Blueprint, jsonify, request
from .models import db, Anime, Manga, SavedAnime, SavedManga
from .utils import cache_response

api = Blueprint('api', __name__)

@api.route('/test')
def test():
    return jsonify({'message': 'API is working!'})

@api.route('/anime', methods=['GET'])
@cache_response
def get_anime():
    anime_list = Anime.query.all()
    return jsonify([anime.to_dict() for anime in anime_list])

@api.route('/anime', methods=['POST'])
def add_anime():
    data = request.json
    new_anime = Anime(**data)
    db.session.add(new_anime)
    db.session.commit()
    return jsonify({'message': 'Anime added successfully'}), 201

@api.route('/manga', methods=['GET'])
@cache_response
def get_manga():
    manga_list = Manga.query.all()
    return jsonify([manga.to_dict() for manga in manga_list])

@api.route('/manga', methods=['POST'])
def add_manga():
    data = request.json
    new_manga = Manga(**data)
    db.session.add(new_manga)
    db.session.commit()
    return jsonify({'message': 'Manga added successfully'}), 201

@api.route('/anime/bulk-upload', methods=['POST'])
def bulk_upload_anime():
    data = request.get_json()
    for entry in data:
        anime = Anime(**entry)
        db.session.add(anime)
    db.session.commit()
    return jsonify({'message': 'Anime data uploaded successfully'}), 201

@api.route('/manga/bulk-upload', methods=['POST'])
def bulk_upload_manga():
    data = request.get_json()
    for entry in data:
        manga = Manga(**entry)
        db.session.add(manga)
    db.session.commit()
    return jsonify({'message': 'Manga data uploaded successfully'}), 201

@api.route('/anime/save', methods=['POST'])
def save_anime():
    data = request.json
    anime_id = data.get('anime_id')
    
    # Check if already saved
    existing = SavedAnime.query.filter_by(anime_id=anime_id).first()
    if existing:
        return jsonify({'message': 'Anime already in your list'}), 400
        
    saved_anime = SavedAnime(anime_id=anime_id)
    db.session.add(saved_anime)
    db.session.commit()
    return jsonify({'message': 'Anime added to your list'}), 201

@api.route('/manga/save', methods=['POST'])
def save_manga():
    data = request.json
    manga_id = data.get('manga_id')
    
    # Check if already saved
    existing = SavedManga.query.filter_by(manga_id=manga_id).first()
    if existing:
        return jsonify({'message': 'Manga already in your list'}), 400
        
    saved_manga = SavedManga(manga_id=manga_id)
    db.session.add(saved_manga)
    db.session.commit()
    return jsonify({'message': 'Manga added to your list'}), 201

@api.route('/saved/anime', methods=['GET'])
def get_saved_anime():
    saved_items = SavedAnime.query.all()
    result = []
    for item in saved_items:
        anime = Anime.query.get(item.anime_id)
        if anime:
            data = anime.to_dict()
            data['saved_id'] = item.id
            data['status'] = item.status
            data['date_added'] = item.date_added.isoformat()
            result.append(data)
    return jsonify(result)

@api.route('/saved/manga', methods=['GET'])
def get_saved_manga():
    saved_items = SavedManga.query.all()
    result = []
    for item in saved_items:
        manga = Manga.query.get(item.manga_id)
        if manga:
            data = manga.to_dict()
            data['saved_id'] = item.id
            data['status'] = item.status
            data['date_added'] = item.date_added.isoformat()
            result.append(data)
    return jsonify(result)
