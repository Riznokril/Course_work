from click import command
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from multiprocessing import Process, Value

from datetime import datetime

import serial.tools.list_ports


#Data for connection to DB URI
dbhost = "localhost:3306"
dbuser = "root"
dbpass = "234432or"
dbname = "course_work_db"
connection_data = "mysql+pymysql://{0}:{1}@{2}/{3}".format(dbuser, dbpass, dbhost, dbname)

#Flask DB configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_data
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#ORM
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45))
    password = db.Column(db.String(45))


    def get_data_dictionary(self):
        return {'Id': self.id, 'name': self.name, 'password': self.password}

    def __repr__(self):
        return "Id: {0}, name: {1}, password: {2}".format(self.id, self.name, self.password)

class User_enter_and_exit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    open_close = db.Column(db.String(1))
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)


    def get_data_dictionary(self):
        return {"Id": self.id, "open_close": self.open_close, "time": self.time, "user_id": self.user_id}

    def __repr__(self):
        return "Id: {0}, open_close: {1}, time: {2}, user_id: {3}".format(self.id, self.open_close, self.time, self.user_id)

#Add new user to db
def add_user(new_user):
    db.session.add(new_user)
    db.session.commit()

def add_user_enter_and_exit(new_user_enter_and_exit):
    db.session.add(new_user_enter_and_exit)
    db.session.commit()

#Read all data from db
def read_all_user_data():
    data = User.query.all()
    result = []
    for dat in data:
        result.append(dat.get_data_dictionary())
    return(result)

def read_all_user_enter_and_exit_data():
    data = User_enter_and_exit.query.all()
    result = []
    for dat in data:
        result.append(dat.get_data_dictionary())
    return(result)

#Find user by password
def find_user_by_password(password):
    found = False
    data = User.query.all()
    for dat in data:
        if dat.password == password:
            found = True
            return dat
    if found == False:
        print("No one")
        return User(id = 0, name = "No one", password = "000")

#Read specific row from db
def read_by_id_user_data(id):
    data = User.query.get(id)
    return data.get_data_dictionary()

def read_by_id_user_enter_and_exit_data(id):
    data = User_enter_and_exit.query.get(id)
    return data.get_data_dictionary()



@app.route("/", methods = ['GET'])
def get():    
    data = read_all_user_enter_and_exit_data()
    #if data.open_close == '0':
    print(data)

    return (jsonify(data))


def open_close_door(user, open_close):
    if user.name != "No one":
        if open_close == "ON":
            open_close = "OFF"
            serialInst.write(open_close.encode('utf-8'))
            now = datetime.now()
            current_datetime = now.strftime("%y-%m-%d %H:%M:%S")            
            add_user_enter_and_exit(User_enter_and_exit(open_close = '0', time = current_datetime, user_id = user.id))

        elif open_close == "OFF":
            open_close = "ON"
            serialInst.write(open_close.encode('utf-8'))
            now = datetime.now()
            current_datetime = now.strftime("%y-%m-%d %H:%M:%S")            
            add_user_enter_and_exit(User_enter_and_exit(open_close = '1', time = current_datetime, user_id = user.id))
            
    return(open_close)





data = []
open_close = "ON"

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portVar = "COM2"

serialInst.baudrate = 9600
serialInst.port = portVar

if(serialInst.isOpen() == False):
    serialInst.open()


if __name__ == '__main__':

    #app.run(debug=True)

    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            number = packet.decode('utf').rstrip('\n\r')
            if number != "#":
                data.append(number)
                print(data)
            else:
                password = data[-3] + data[-2] + data[-1]
                user = find_user_by_password(password)
                print(user.name)
                open_close = open_close_door(user, open_close)




        
