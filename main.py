import firebase_admin
import pyrebase
from firebase_admin import db

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
};

default_app = pyrebase.initialize_app(firebaseConfig)
# default_app = pyrebase.initialize_app(cred_obj, {
#     'databaseURL': "https://numpad-proj-default-rtdb.europe-west1.firebasedatabase.app"
# })

db = default_app.database()
user_key = "yakir"
#
# ref = db.reference("/Users")
# ref.child(user_key).set({"last": "num1"})
#
# ref = db.reference("/Users/" + user_key)
# print(ref.get()["last"])


def stream_handler(message):
    # print(message["event"])
    # print(message["path"])
    print(message["data"])


my_stream = db.child("/Users/" + user_key).stream(stream_handler)
