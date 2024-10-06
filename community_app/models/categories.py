from community_app import db


class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    questions = db.relationship('Questions', backref='category', lazy=True)

    def __str__(self):
        return f"Category: {self.name}"
