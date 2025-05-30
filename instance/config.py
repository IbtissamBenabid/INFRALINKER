import os

user = os.environ.get("MYSQL_USER", "admin_db")
password = os.environ.get("MYSQL_PASSWORD", "admin_db_password")

SECRET_KEY = os.urandom(24)
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@localhost:3306/infralinker_db"

SQLALCHEMY_POOL_RECYCLE = 60
