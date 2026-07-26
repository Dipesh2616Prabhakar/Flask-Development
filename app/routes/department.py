from flask import Blueprint, render_template
from app.models.employee import Employee
from app.models import db

department_bp = Blueprint("department", __name__)

@department_bp.route("/department")
def departmentHome():
    results = (
        db.session.query(Employee.department, db.func.count(Employee.id), db.func.avg(Employee.salary))
        .group_by(Employee.department)
        .all()
    )
    departments = [
        {"name": name, "count": count, "avg_salary": round(avg or 0, 2)}
        for name, count, avg in results
    ]
    return render_template("department.html", departments=departments)