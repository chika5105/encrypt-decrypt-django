import unittest
from has_seen import UserHasSeen

test = UserHasSeen()
print(test.dic)
class UserHasSeenTests(unittest.TestCase):
    def test_empty_dictionary(self):
        self.assertEqual(test.has_seen('123', '345'), False)
        print(test.dic)

    def test_question_not_in_dic(self):
        self.assertEqual(test.insert('123','345'),None)
        print(test.dic)
    def test_question_and_user_in_dic(self):
        self.assertEqual(test.has_seen('123', '345'), True)
        print(test.dic)
    def test_add_user_to_question(self):
        self.assertEqual(test.insert('123', '445'), None)
        print(test.dic)
    def test_new_user_added(self):
        self.assertEqual(test.has_seen('123', '445'), True)
        print(test.dic)
    def test_user_not_seen(self):
        self.assertEqual(test.has_seen('123', '909'), False)
        print(test.dic)
    def test_delete_user_from_question(self):
        self.assertEqual(test.delete_user('345'), None)
        print(test.dic)
    def test_deleted_user_not_seen(self):
        self.assertEqual(test.has_seen('123', '345'), False)
        print(test.dic)
    def test_add_new_question_and_user(self):
        self.assertEqual(test.insert('569', '789'), None)
        print(test.dic)
    def test_new_question_and_user(self):
        self.assertEqual(test.has_seen('569', '789'), True)
        print(test.dic)
    def test_deleted_question_and_user(self):
        self.assertEqual(test.delete_question('123'), None)
        print(test.dic)
    def test_question_not_in_dic(self):
        self.assertEqual(test.question_available('123'), False)
        print(test.dic)
    def test_user_not_seen_available_question(self):
        self.assertEqual(test.has_seen('890', '909'), False)
        print(test.dic)
    


if __name__ == '__main__':
    unittest.main()

