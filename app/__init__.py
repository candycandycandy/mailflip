from flask import Flask

def create_app():
	app = Flask(__name__)

	@app.route("/", methods=['GET'])
	def index():
	    return "MailFlip!"

	return app