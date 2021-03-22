from app import app
import sshtunnel
from password import *

on_pythonanywhere = not (__name__ == '__main__')

print("site pass: ", ACCOUNT_PASS)
print("db pass: ", DB_PASS)

if on_pythonanywhere:    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner.mysql.pythonanywhere-services.com'
    
# local environment
else:   
    tunnel = sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='KSUCoursePlanner', ssh_password=DB_PASS,
        remote_bind_address=('KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
    )

    tunnel.start()

    # config to get in the main frame
    conn = 'mysql://KSUCoursePlanner:{}@127.0.0.1:{}/KSUCoursePlanner$test'.format(ACCOUNT_PASS, tunnel.local_bind_port)
    print(conn)
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    

# turn off depreciation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if not on_pythonanywhere:
    app.run()