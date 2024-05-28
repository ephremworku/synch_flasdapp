import os

class Config:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'flask_app.db')
    DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
