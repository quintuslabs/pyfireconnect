from setuptools import setup, find_packages

setup(
    name='pyfirebase',
    version='1.0.0',
    url='https://github.com/quintuslabs/pyfirebase',
    description='A simple python wrapper for the Firebase API, originally forked from https://github.com/thisbejim/pyfirebase and now compatible with Python 3.7',
    author='Quintus Labs',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=('Firebase','Python 3',),
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests==2.22.0',
        'gcloud==0.18.3',
        'oauth2client==4.1.3',
        'requests_toolbelt==0.9.1',
        'python_jwt==3.2.4',
        'pycryptodome==3.9.0',
        'urllib3==1.25.5'
    ]
)
