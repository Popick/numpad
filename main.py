import firebase_admin
import pyrebase
from firebase_admin import db
import keyboard

cred_obj = firebase_admin.credentials.Certificate('F:/Shit/numpad-proj-firebase-adminsdk-7hblg-17058afaf6.json')
firebaseConfig = {
    "apiKey": "AIzaSyDZYIAHveRTpk6z290r3wg0XYn6kzLkcmM",
    "authDomain": "numpad-proj.firebaseapp.com",
    "databaseURL": "https://numpad-proj-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "numpad-proj",
    "storageBucket": "numpad-proj.appspot.com",
    "messagingSenderId": "686812330595",
    "appId": "1:686812330595:web:b60e00ab3acd5fa996d656",
    "measurementId": "G-VJT8BEYC1M"
}

default_app = pyrebase.initialize_app(firebaseConfig)

db = default_app.database()
user_key = "yakir"
global key_to_write


def stream_handler(message):
    # print(message["event"])

    # print(message["path"])
    key_to_write = message["data"]["lastKey"]

    writeKey(key_to_write)


my_stream = db.child("/Users/" + user_key).stream(stream_handler)

temp_key = ""
def writeKey(key_to_write):
    print(key_to_write)
    if key_to_write == "enter":
        keyboard.send("enter")
    elif key_to_write == "backspace":
        keyboard.send("backspace")
    elif key_to_write == "right":
        keyboard.send("right")
    elif key_to_write == "left":
        keyboard.send("left")
    else:
        keyboard.write(key_to_write)


