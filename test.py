import os
import unittest
import sys
import requests


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from app import app, db

test_db = "test_db"

class elemTests(unittest.TestCase):
    def setUp(self):
        '''
            This method sets up the tests 
        '''
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def shutDown(self):
        '''
            This methods shuts down the tests after being completed 
        '''
        pass

    def test_main_page(self):
        '''
          This method verifies that the home page is successfuly loaded.
        '''
        req = self.app.get('/main', follow_redirects=True)
        self.assertEqual(req.status_code, 200)

    def test_login(self):
        '''
            This method verifies that login page is shown whenever the user is not logged in
        '''
        req = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(req.url, 'http://127.0.0.1:5000/signin')

    def test_signup(self):
        '''
            This method verisies that registration has been successfully completed
            that user are redirected to index page.
        '''
        details = {'username':'Hamidli', 'password':'Minerva2023', 'repeat':'Minerva2023'}
        req = requests.post('http://127.0.0.1:5000/signup', data = details)
        req = requests.post('http://127.0.0.1:5000/signin', data = details)
        self.assertEqual(req.url, 'http://127.0.0.1:5000/main')


    def test_success_login(self):
        '''
            This method verifies that users credinatial are coorect. 
        '''
        details = {'username':'Hamidli',  'password':'Minerva2023'}
        req = requests.post('http://127.0.0.1:5000/signin', data = details)
        self.assertEqual(req.url, 'http://127.0.0.1:5000/main')


    def test_unsuccess_login(self):
        '''
            This method verifies that user with wrong input to not proceed
        '''
        details = {'username':'Hamidli', 'password':'Minerva2023'}
        req = requests.post('http://127.0.0.1:5000/signin', data = details)
        self.assertEqual(req.url, 'http://127.0.0.1:5000/signin')


if __name__ == "__main__":
    unittest.main()





