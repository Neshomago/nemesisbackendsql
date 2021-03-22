from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'atorres1986'
app.config['MYSQL_DATABASE_DB'] = 'nemesis'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['UPLOAD_EXCEL'] = './excel'
mysql.init_app(app)
