from pyfireconnect import pyfireconnect
from pyfireconnect.pyfireconnect import REQUEST_TYPE

SIMPLE_CONFIG = {
    "apiKey" : "AIzaSyA2Ok_NIHj5OF7-sevl8wegH73XXZpMoJ4",
    "authDomain" : "wiallow.firebaseapp.com",
    "databaseURL": "https://wiallow.firebaseio.com",
    "projectId" : "wiallow",
    "storageBucket": "",
    "messagingSenderId" : "408646127681",
    "appId" : "1:408646127681:web:68051044b77016703276c0"
}

firebase = pyfireconnect.initialize(SIMPLE_CONFIG)

auth = firebase.auth()
#user = auth.sign_in_with_email_and_password("pani.shiv@gmail.com", "Welcome123")

reset_password_response = auth.send_password_reset_email("pani.shiv@gmail.com")

#change_password_response = auth.change_password(user['idToken'], "Welcome123")

print(reset_password_response)

# db = firebase.database()
# data = {
#     "name": "Mortimer 'Morty' Smith"
# }
# db.child("Tummy27").push(data, user['idToken'])