from flask import Blueprint, request, jsonify
from models import db, Employee
from auth import token_required

employee_bp = Blueprint(
    "employees",
    __name__,
    url_prefix="/api/employees"
)

# CREATE
@employee_bp.route("/", methods=["POST"])
@token_required
def create_employee():
    data = request.json

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400

    if Employee.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400

    emp = Employee(
        name=data["name"],
        email=data["email"],
        department=data.get("department"),
        role=data.get("role")
    )

    db.session.add(emp)
    db.session.commit()
    return jsonify(emp.to_dict()), 201


# LIST + FILTER + PAGINATION
@employee_bp.route("/", methods=["GET"])
@token_required
def list_employees():
    department = request.args.get("department")
    role = request.args.get("role")
    page = int(request.args.get("page", 1))

    query = Employee.query
    if department:
        query = query.filter_by(department=department)
    if role:
        query = query.filter_by(role=role)

    result = query.paginate(page=page, per_page=10, error_out=False)

    return jsonify({
        "total": result.total,
        "page": page,
        "employees": [e.to_dict() for e in result.items]
    })


# GET BY ID
@employee_bp.route("/<int:id>/", methods=["GET"])
@token_required
def get_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(emp.to_dict())


# UPDATE
@employee_bp.route("/<int:id>/", methods=["PUT"])
@token_required
def update_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    data = request.json
    emp.name = data.get("name", emp.name)
    emp.department = data.get("department", emp.department)
    emp.role = data.get("role", emp.role)

    db.session.commit()
    return jsonify(emp.to_dict())


# DELETE
@employee_bp.route("/<int:id>/", methods=["DELETE"])
@token_required
def delete_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(emp)
    db.session.commit()
    return "", 204
