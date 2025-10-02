from flask import Blueprint, request, jsonify
from extensions import db
from models import Trainer
from flask_jwt_extended import jwt_required

trainer_bp = Blueprint('trainer_bp', __name__)

@trainer_bp.route('/', methods=['GET'])
def get_trainers():
    trainers = Trainer.query.all()
    result =[]
    for t in trainers:
        result.append({
            'id': t.id,
            'name': t.name,
            'bio': t.bio,
            'speciality':t.speciality,
            'image_url': t.image_url
        })
    return jsonify(result), 200

@trainer_bp.route('/<int:trainer_id>', methods=["GET"])
def get_trainer(trainer_id):
    t =Trainer.query.get(trainer_id)
    if not t:
        return jsonify({"msg": "trainer not found "}), 404
    return jsonify ({
        "id":t.id,
        "name":t.name,
        "bio": t.bio,
        "speciality":t.speciality,
        "image_url": t.image_url,
    }),200    
     
