from sql_alchemy import banco
from models.point import PointModel

class EmployeeModel(banco.Model):
  __tablename__ = 'employees'

  id = banco.Column(banco.Integer, primary_key=True)
  name = banco.Column(banco.String)
  function = banco.Column(banco.String)
  points = banco.relationship("PointModel")

  def __init__(self, name, function):
    self.name = name
    self.function = function
  
  def json(self):
    return {
      'id' : self.id,
      'name' : self.name,
      'function' : self.function,
      'points' : [point.json() for point in self.points]
    }
  
  def find_employee(self, id):
    employee = banco.Query.filter_by(id=id).first()
    if employee:
      return employee
    return None
  
  def find_employee_name(self, name):
    employee = banco.Query.filter_by(name=name).first()
    if employee:
      return employee
    return None

  def save(self):
    banco.session.add(self)
    banco.session.commit()
  
  def update(self, name, function):
    self.name = name
    self.function = function

  def delete(self):
    banco.session.delete(self)
    banco.session.commit()