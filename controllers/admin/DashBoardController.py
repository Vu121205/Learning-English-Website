from flask import Blueprint, Flask, app, render_template

dashBoard_bp = Blueprint('dashboard', __name__)

@dashBoard_bp.route('/admin')
def home():
    return render_template('admin/dashboard.html')