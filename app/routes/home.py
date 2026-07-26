from flask import Blueprint, render_template
from app.models.employee import Employee
from app.models import db

home_bp = Blueprint("home", __name__)

@home_bp.route("/home")
def home():
    total_employees = Employee.query.count()
    total_departments = db.session.query(Employee.department).distinct().count()
    return render_template(
        "home.html",
        total_employees=total_employees,
        total_departments=total_departments
    )
@home_bp.route("/")
def index():
    from flask import redirect, url_for
    return redirect(url_for("home.home"))