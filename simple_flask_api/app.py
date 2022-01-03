from flask import Flask
import getpass
user_name = getpass.getuser()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, lets upgrade ! its magic word !World!</p>"

# @app.route("/welcome")
# def welcome():
#     return f'<p>Hello, WELCOME !World{user_name}!</p>'

@app.route("/datetime")
def welcome():
    return f'<p>Hello, WELCOME TO THE STRAPI WORLD!!!!!   {user_name}!</p>'



if __name__ == '__main__':
   app.run(debug=True)

  