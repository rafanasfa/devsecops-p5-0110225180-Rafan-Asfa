from flask import Blueprint, jsonify
from src.user_service import get_all_users, get_user_by_id

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def fetch_users():
    return jsonify({"status": "success", "data": get_all_users()}), 200

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def fetch_user_by_id(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404
    return jsonify({"status": "success", "data": user}), 200