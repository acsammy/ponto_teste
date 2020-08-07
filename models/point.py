from sql_alchemy import banco

class PointModel(banco.Model):
  __tablename__ = 'points'

  id = banco.Column(banco.Integer, primary_key=True)
  date = banco.Column(banco.String)
  hour = banco.Column(banco.String)
  employee_id = banco.Column(banco.ForeignKey('employees.id'))

  def __init__(self, date, hour, employee_id):
    self.date = date
    self.hour = hour
    self.employee_id = employee_id
  
  def json(self):
    return {
      'id' : self.id,
      'date' : self.date,
      'hour' : self.hour,
      'employee_id' : self.employee_id
    }
  
  @classmethod
  def find_point(cls, id):
    point = cls.query.filter_by(id=id).first()
    if point:
      return point
    return None

  @classmethod
  def find_day(cls, date):
    points = cls.query.filter_by(date=date)
    if points:
      return points
    return None

  def save(self):
    banco.session.add(self)
    banco.session.commit()
  
  def update(self, date, hour):
    self.date = date
    self.hour = hour
  
  def delete(self):
    banco.session.delete(self)
    banco.session.commit()