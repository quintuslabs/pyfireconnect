SIMPLE_CONFIG = {
    "apiKey": "apiKey",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "projectId.appspot.com",
    "serviceAccount": "path/to/serviceAccountCredentials.json"
}

SERVICE_ACCOUNT_PATH = "secret.json"

SERVICE_CONFIG = dict(SIMPLE_CONFIG, serviceAccount=SERVICE_ACCOUNT_PATH)
