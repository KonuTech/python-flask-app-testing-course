from models.user import UserModel
from test.unit.unit_base_test import UnitBaseTest

class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModelq('test', 'abcd')

        self.assertEqual(user.username, 'test', )
        self.assertEqual(user.username, 'abcd', )
