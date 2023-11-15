from json import dumps
from flask import Blueprint
from app.services.user_service import UserService

user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.route("/home")
def home():
    return "Hello World!"


@user_blueprint.route("/")
def get_users():
    users = UserService.get_users()
    user_list = [{"name": user["name"], "email": user["email"]} for user in users]
    
    response_data = {
        "message": "User list has been fetched successfully.",
        "success": True,
        "result": {"data": user_list},
    }
    return dumps(response_data)


@user_blueprint.route("/create", methods=["POST"])
def create_user():
    try:
        data = {"name": "Tony Stark", "email": "stark@gmail.com"}
        UserService.create_user(data)
    except Exception as e:
        data = {"error": str(e)}

    response_data = {
        "message": "User created successfully.",
        "success": True,
        "result": {"data": data},
    }
    return dumps(response_data, default=str)
