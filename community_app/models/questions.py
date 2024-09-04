from community_app import db

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(300), nullable = False)
    responses = db.relationship("Responses", backref = 'question')
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __str__(self):
        return f"Question: {self.text}"


class Statistics(db.Model):
    __tablename__ = 'statistics'
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key = True)
    agree_count = db.Column(db.Integer, default = 0)
    disagree_count = db.Column(db.Integer, default = 0)

    def __str__(self):
        return (f"Statistics for questions {self.question_id} "
                f"Agree: {self.agree_count}, "
                f"Disagree: {self.disagree_count}")


