
import unittest

from app.models import Podcast, User
from app import db, create_app 
from config import Config

class testConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"

class UserTesting(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app(testConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        return self.app_context.pop()
    
    def test_password_hashing(self):
        user = User()
        user.set_password("Cat")
        self.assertFalse(user.check_password("Dog"), "Password hashing detects failure correctly")
        self.assertTrue(user.check_password("Cat"), "Password hashing detects success correctly")

if __name__ == '__main__':
    unittest.main()
