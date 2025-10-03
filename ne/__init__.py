from flask import Flask
from dotenv import load_dotenv

from ne import pages, messages, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)

    app.register_blueprint(messages.bp)
    app.register_blueprint(pages.bp)
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app
