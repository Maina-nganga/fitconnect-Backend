from flask import Blueprint, request, jsonify
from extensions import db
from models import Enquiry, Trainer
from flask_jwt_extended import jwt_required

enquiry_bp = Blueprint("enquiry_bp", __name__)

@enquiry_bp.route("/", methods=["POST"])
def create_enquiry():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    trainer_id = data.get("trainer_id")

    if not name or not email or not message:
        return jsonify({"msg": "Missing fields"}), 400

    if trainer_id:
        trainer = Trainer.query.get(trainer_id)
        if not trainer:
            return jsonify({"msg": "Invalid trainer ID"}), 400
    else:
        trainer = None

    enq = Enquiry(
        name=name,
        email=email,
        message=message,
        trainer_id=trainer.id if trainer else None  # ✅ correct FK handling
    )
    db.session.add(enq)
    db.session.commit()

    return jsonify({"msg": "Enquiry saved", "id": enq.id}), 201


@enquiry_bp.route("/", methods=["GET"])
@jwt_required()
def list_enquiries():
    enquiries = Enquiry.query.order_by(Enquiry.created_at.desc()).all()  # ✅ fixed field name
    out = []
    for en in enquiries:
        out.append({
            "id": en.id,
            "name": en.name,
            "email": en.email,
            "message": en.message,
            "created_at": en.created_at.isoformat(),  # ✅ fixed
            "trainer_id": en.trainer_id
        })
    return jsonify(out), 200
