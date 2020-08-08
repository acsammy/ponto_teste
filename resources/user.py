from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp

attributes = reqparse.RequestParser()
attributes.add_argument('name', type=str)
attributes.add_argument('email', type=str, required=True, help="Email is required.")
attributes.add_argument('password', type=str, required=True, help="Password is required.")

class Users(Resource):
  def get(self):
    return {
      'users' : [user.json() for user in UserModel.query.all()]
    }

class User(Resource):
  def get(self, id):
    user = UserModel.find_user(id)
    if(user):
      return user.json()
    return { 'message' : 'User not found.' }, 404
  
  def delete(self, id):
    user = UserModel.find_user(id)
    if user:
      user.delete()
      return {
        'message' : 'User deleted successfuly.'
      }
    return {
      'message' : 'User not found'
    }, 404
  
class UserRegister(Resource):
  def post(self):
    data = attributes.parse_args()
    if UserModel.find_by_email(data['email']):
      return { 
        'message' : 'Email {} already exists'.format(data['email'])
      }, 400
    
    user = UserModel(**data)

    try:
      user.save()
    except:
      return {
        'message' : 'An error ocurred trying to create user'
      }, 500
    return user.json(), 201

class UserLogin(Resource):
  @classmethod
  def post(cls):
    data = attributes.parse_args()
    user = UserModel.find_by_email(data['email'])
    if user and safe_str_cmp(user.password, data['password']):
      token = create_access_token(identity=user.id)
      return {
        'token' : token
      }, 200
    return {
      'message' : 'Email or password is incorrect.'
    }, 401