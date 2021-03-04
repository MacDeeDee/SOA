from flask import Flask, render_template
# from display import display
from flaskwebgui import FlaskUI

app = Flask(__name__)
# app.register_blueprint(display)
desktopApp = FlaskUI(app)

@app.route('/')
def displayScreen():
    return render_template('/getStudent.html')

if __name__ == '__main__':

    '''app.run(host='localhost', port='8000', debug=True)'''
    # getStudentBySID()
    desktopApp.localhost = "http://127.0.0.1:8000/"
    desktopApp.port = 8000
    desktopApp.run()

