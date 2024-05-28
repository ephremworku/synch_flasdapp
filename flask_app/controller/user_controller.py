from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/fill_form')
def fill_form():
    return render_template('register.html')

@user_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        fav_prog_language = request.form.get('favprogramminglan')
        sex = request.form.get('sex')
        
        if not username or not email:
            return jsonify({'error': 'Invalid input'}), 400
        
        try:
            UserService.create_user(username, email, fav_prog_language, sex)
            return redirect(url_for('user.success'))
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'The request needs to be Post': "none Post request made"})




@user_bp.route('/success')
def success():
    return "Form submitted successfully!"
