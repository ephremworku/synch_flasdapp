from flask import Flask, render_template, request, redirect
from config import Config
from adapters.database import init_db
from controller.user_controller import user_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
init_db(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/users')
@app.route('/')
def fill_form():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
