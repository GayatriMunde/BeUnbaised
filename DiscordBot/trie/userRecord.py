class UserRecord:
    user_record = dict()

    def check_record(self, author_id):
        return self.user_record[author_id] >= 3

    def add_record(self, author_id):
        if author_id in self.user_record.keys():
            self.user_record[author_id] += 1
        else:
            self.user_record[author_id] = 0
