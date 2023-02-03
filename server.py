from flask_app import app 
#this is where we import controllers when we make it
from flask_app.controller import login_controller
#ALL CONTROLLERS ARE IMPORTED HERE

if __name__=="__main__":
    app.run(debug=True,port=5001)
