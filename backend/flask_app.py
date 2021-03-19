from app import app
import sshtunnel

# db connect
if __name__ == '__main__':    # local instance
    # the connection stuff here through sshtunnel 
    tunnel = sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='KSUCoursePlanner', ssh_password='N5L3TR8mHq',
        remote_bind_address=('KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
    )

    # starts the tunnel
    tunnel.start()

    # config to get in the main frame
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner:QMX4e6%nh!5[@127.0.0.1:{}/KSUCoursePlanner$test'.format(tunnel.local_bind_port)

else:   # pythonanywhere
    # connect to mysql
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner.mysql.pythonanywhere-services.com'

# turn off depreciation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run()