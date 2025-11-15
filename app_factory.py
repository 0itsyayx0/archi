from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

# blueprints
from controllers.celulares_controllers import celulares_bp
from controllers.user_controllers import auth_bp
from controllers.marcas_controllers import marcas_bp




def create_app():
	app = Flask(__name__, static_folder='frontend', static_url_path='')
	# configuración mínima
	app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-for-testing')
	# permitir CORS para desarrollo
	CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

	# Asegurar cabeceras CORS en todas las respuestas (refuerzo en caso de servidores estáticos/preflight)
	@app.after_request
	def add_cors_headers(response):
		response.headers.setdefault('Access-Control-Allow-Origin', '*')
		response.headers.setdefault('Access-Control-Allow-Headers', 'Content-Type,Authorization')
		response.headers.setdefault('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
		return response
	JWTManager(app)

	# Servir archivos estáticos frontend
	@app.route('/')
	def serve_index():
		return send_from_directory(app.static_folder, 'index.html')

	@app.route('/<path:path>')
	def serve_static(path):
		if os.path.exists(os.path.join(app.static_folder, path)):
			return send_from_directory(app.static_folder, path)
		return send_from_directory(app.static_folder, 'index.html')

	# registrar blueprints
	app.register_blueprint(celulares_bp)
	app.register_blueprint(auth_bp)
	app.register_blueprint(marcas_bp)

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(host='127.0.0.1', port=5000, debug=True)
