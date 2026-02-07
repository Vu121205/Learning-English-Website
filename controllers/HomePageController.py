from flask import Blueprint, Flask, app, render_template

home_page_bp = Blueprint('home_page', __name__)

@home_page_bp.route('/admin')
def home_page():
    return render_template('admin/dashboard.html')