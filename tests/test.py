from pyfireconnect import pyfireconnect

SIMPLE_CONFIG = {
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