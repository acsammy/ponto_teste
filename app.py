from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import Users, User, UserRegister, UserLogin
from resources.employee import EmployeeModel, Employees, Employee
from resources.point import Point, PointModel, PointstDay

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5533/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
  banco.create_all()



#routes
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

api.add_resource(Employee, "/employees, /employees/<int:id>") # cadastra funcionario
api.add_resource(Employees, '/employees') # retorna todos funcionarios
api.add_resource(Employee, ) # retorna funcionario especifico
api.add_resource(PointstDay, '/employees/<int:id>/<string:date>') # retorna funcionario e pontos do dia

#api.add_resource(Points, '/points')
api.add_resource(Point, '/points')

if(__name__ == '__main__'):
  from sql_alchemy import banco
  banco.init_app(app)
  app.run(port=5000)