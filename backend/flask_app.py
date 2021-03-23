from app import app
import sshtunnel


on_pythonanywhere = not (__name__ == '__main__')

if on_pythonanywhere:    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner.mysql.pythonanywhere-services.com'
    
# local environment
else:   
    from password import *

    tunnel = sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='KSUCoursePlanner', ssh_password=ACCOUNT_PASS,
        remote_bind_address=('KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
    )

    tunnel.start()

    # config to get in the main frame
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner:{}@127.0.0.1:{}/KSUCoursePlanner$test'.format(DB_PASS, tunnel.local_bind_port)

# turn off depreciation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if not on_pythonanywhere:
    app.run()