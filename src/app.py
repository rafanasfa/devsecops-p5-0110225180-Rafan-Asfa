from flask import Flask, jsonify
from src.routes import api_bp

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({"message": "DevSecOps Python Practice API is running"}), 200

    app.register_blueprint(api_bp, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)