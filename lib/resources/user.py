from flask_restful import Resource, reqparse
from flask_bcrypt import check_password_hash, generate_password_hash
from pymongo import MongoClient
from models.user_model import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token,
        jwt_required, jwt_refresh_token_required, get_jwt_identity)

parser = reqparse.RequestParser()
parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
 
class UserRegister(Resource):
       def post(self):
        data = parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with this email already exists"}, 400
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with this username already exists"}, 400

        password_hash = generate_password_hash(data['password']).decode('utf-8')
        user = UserModel(data['email'], data['username'], password_hash)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()

        user = UserModel.find_by_email(data['email'])
        if user and check_password_hash(user['password'], data['password']):
            access_token = create_access_token(identity=user.email, fresh=True)
            refresh_token = create_refresh_token(identity=user.email)
            return {'access_token': access_token, 'refresh_token': refresh_token}, 200
        else:
            return {'message': 'invalid username or password'}, 401

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200