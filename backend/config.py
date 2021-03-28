import os
import sshtunnel

def connect_to_db_locally():
    tunnel = sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='KSUCoursePlanner', 
        ssh_password=os.environ.get('ACCOUNT_PASS'),
        remote_bind_address=(
            'KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
    )

    tunnel.start()
    return tunnel


def get_local_conn_string():
    tunnel = connect_to_db_locally()
    return 'mysql://KSUCoursePlanner:{}@127.0.0.1:{}/KSUCoursePlanner$test'.format(
        os.environ.get('DB_PASS'), tunnel.local_bind_port)


def get_prod_conn_string():
    return "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="KSUCoursePlanner",
        password=os.environ.get('DB_PASS'),
        hostname="KSUCoursePlanner.mysql.pythonanywhere-services.com",
        databasename="KSUCoursePlanner$test"
    )

# base config regardless of environment
class Config(object):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_prod_conn_string()
    FRONTEND_URL = "https://ksucourseplanner.pythonanywhere.com/#"
    SECRET_KEY = os.environ.get('API_KEY')


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_local_conn_string()
    FRONTEND_URL = "http://localhost:8080/#"
