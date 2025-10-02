from flask import Flask
from config import Config
from extensions import db, migrate, jwt, cors
from routes.auth import auth_bp
from routes.trainer import trainer_bp
from routes.enquiry import enquiry_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

   
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

 
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(trainer_bp, url_prefix='/api/trainers')
    app.register_blueprint(enquiry_bp, url_prefix='/api/enquiries')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



