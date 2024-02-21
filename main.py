#import flask
from flask import Flask
import socket
app=Flask(__name__)

@app.route("/welcome")
def welcome():
    coolspear="How are you Bisi"
    
    # Json code to list employee scores

    return ("welcome to London bisi")


if __name__== '__main__':
    app.run(debug=True, host="127.0.0.1", port=5005)
