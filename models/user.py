from sql_alchemy import banco

class UserModel(banco.Model):
  __tablename__ = 'users'

  id = banco.Column(banco.Integer, primary_key=True)
  name = banco.Column(banco.String)
  email = banco.Column(banco.String)
  password = banco.Column(banco.String)
  admin = banco.Column(banco.Integer)

  def __init__(self, name, email, password, admin):
    self.name = name
    self.email = email
    self.password = password
    self.admin = 0
  
  def json(self):
    return {
      'id' : self.id,
      'name' : self.name,
      'email' : self.email,
      'admin' : self.admin
    }
  
  @classmethod
  def find_user(cls, id):
    user = cls.query.filter_by(id=id).first()
    if(user):
      return user
    return None
  
  @classmethod
  def find_by_email(cls, email):
    user = cls.query.filter_by(email=email).first()
    if user:
      return user
    return None

  def save(self):
    banco.session.add(self)
    banco.session.commit()

  def update(self, name, email, password, admin):
    self.name = name
    self.email = email
    self.password = password
    self.admin = admin

  def delete(self): 
    banco.session.delete(self)
    banco.session.commit()