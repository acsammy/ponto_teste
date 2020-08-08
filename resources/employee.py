from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.employee import EmployeeModel

attributes = reqparse.RequestParser()
attributes.add_argument('name', type=str, required=True)
attributes.add_argument('function', type=str, required=True)

class Employees(Resource):
  @jwt_required
  def get(self):
    return {
      'employees' : [employee.json() for employee in EmployeeModel.query.all()]
    }

class Employee(Resource):
  @jwt_required
  def post(self):
    data = attributes.parse_args()
    if EmployeeModel.find_employee_name(data.get('name')):
      return {
        'message' : 'Employee {} already exists.'.format(data.get('name'))
      }, 404
    
    employee = EmployeeModel(**data)

    try:
      employee.save()
    except:
      return {
        'message' : 'An error occured trying to create employee.'
      },500
    return employee.json(), 201

  @jwt_required
  def get(self, id):
    employee = EmployeeModel.find_employee(id)
    if employee:
      return employee.json()
    return {
      'message' : 'Employee not found.'
    }, 404

  @jwt_required
  def put(self, id):
    employee = EmployeeModel.find_employee(id)
    if employee:
      data = attributes.parse_args()
      employee.update(**data)
      try:
        employee.save()
      except:
        return {
          'message' : 'An error occured trying to update Employee.'
        }
    return employee.json()
    
  @jwt_required  
  def delete(self, id):
    employee = EmployeeModel.find_employee(id)
    if employee:
      employee.delete()
      return {
        'message' : 'Employee deleted successfuly.'
      }, 200
    return {
      'message' : 'Employee not found.'
    }, 404