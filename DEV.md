Developing
==========

python setup.py sdist bdist_wheel



twine upload dist/pyfireconnect-1.0.2.tar.gz
python setup.py sdist


Create a new virtualenv and install the required libraries for
the default pyfireconnect + the testing tools.

```
mkvirtualenv -p python3 pyfireconnect-dev # if you have virtualenvwrapper installed
pip install -r requirements.txt -r requirements.dev.txt
```

Configure a test database

```
cp ~/my_secret_firebase_service_account_key.json ./secret.json
cp ./tests/config.template.py ./tests/config.py
# Update the ./tests/config.py file with your test database.
```

Note that to make it easier to run the tests, they read/write to
`/pyfireconnect_tests/` on your firebase database. They should not mess
up the rest of the database.


Run the tests:

```
pytest -s tests
```

On MacOS you may need to fix the shebang in the pytest executable
to make it point to the correct python binary.
