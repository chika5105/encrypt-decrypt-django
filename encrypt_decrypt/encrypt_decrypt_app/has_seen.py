
class UserHasSeen:
    def __init__(self):
        self.dic = {}

    def insert(self, question_id, user_id):
        if not self.question_available(question_id):
            self.dic[question_id] = {user_id}
        else:
            self.dic[question_id].add(user_id)
        return

    def delete_user(self, user_id):
        for question in self.dic:
            self.dic[question].discard(user_id)
        return

    def delete_question(self, question_id):
        del(self.dic[question_id])
        return

    def question_available(self, question_id):
        return question_id in self.dic
        
    def has_seen(self, question_id, user_id):
        if self.question_available(question_id):
            return user_id in self.dic[question_id]
        else:
            return False

    def __str__(self):
         return '\n'.join([str(self.dic[j]) for j in (self.dic)])

