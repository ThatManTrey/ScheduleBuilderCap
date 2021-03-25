from app import app
import sshtunnel
from password import *

on_pythonanywhere = not (__name__ == '__main__')

if on_pythonanywhere:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="KSUCoursePlanner",
        password=DB_PASS,
        hostname="KSUCoursePlanner.mysql.pythonanywhere-services.com",
        databasename="KSUCoursePlanner$test",
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    
# local environment
else:
    tunnel = sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='KSUCoursePlanner', ssh_password=ACCOUNT_PASS,
        remote_bind_address=(
            'KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
    )

    tunnel.start()

    # config to get in the main frame
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner:{}@127.0.0.1:{}/KSUCoursePlanner$test'.format(
        DB_PASS, tunnel.local_bind_port)

# turn off depreciation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if not on_pythonanywhere:
    app.run(debug=True)
