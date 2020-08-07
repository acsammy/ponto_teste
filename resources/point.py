from sql_alchemy import banco
from flask_restful import Resource, reqparse
from models.point import PointModel
from models.employee import EmployeeModel

attributes = reqparse.RequestParser()
attributes.add_argument('date', type=str, required=True)
attributes.add_argument('hour', type=str, required=True)
attributes.add_argument('employee_id', type=int)

class Point(Resource):
  def post(self):
    data = attributes.parse_args()
    if not EmployeeModel.find_employee(data.get('employee_id')):
      return {
        'message' : 'Employee not found.'
      }, 400

    points = PointModel.find_day(data.get('date'))
    if (len(points) >= 6):
      return {
        'message' : 'You can`t register more than six points per day.'
      }, 400
    point = PointModel(**data)
    
    try:
      point.save()
    except:
      return {
        'message' : 'An error acurred while saving point.'
      }, 400
    return point.json()

class PointstDay(Resource):
  def get(self, date):
    return date
    points = PointModel.find_day(date)
    if points:
      return {
        'points' : [point.json() for point in points]
      }, 200
    return {
      'message' : 'The date {} selected doesn`t have points'.format(date)
    }, 400