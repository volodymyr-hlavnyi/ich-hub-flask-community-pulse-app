from Communuity_pulse_app import db

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(300), nullable = False)

    responses = db.relationship("Responses", backref = 'question')

    def __str__(self):
        return f"Question: {self.text}"


class Statistics(db.Model):
    __tablename__ = 'statistics'
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key = True)


