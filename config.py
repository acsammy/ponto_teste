import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  """Base configuration"""

  user = 'postgres',
  password = 'postgres',
  hostname = 'localhost',
  port = 5432,
  database = 'company'

  SQLALCHEMY_DATABASE_URI = (
      f"postgresql://{user}:{password}@{hostname}:{port}/{database}"
  )
  SQLALCHEMY_TRACK_MODIFICATIONS = False