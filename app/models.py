from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# creates the users table
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)

    notes = db.relationship('Note', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }


# create the notebooks table
class NoteBook(db.Model):
    __tablename__ = 'notebooks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # creates the relationship to the users table
    user = db.relationship('User')
    notes = db.relationship('Note', back_populates='notebook')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
        }


# create notes table
class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, default='Untitled')
    content = db.Column(db.Text)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebooks.id'), nullable=False)

    notebook = db.relationship('Notebook', back_populates='notes')
    user = db.relationship('User', back_populates='notes')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'notebook_id': self.notebook_id,
        }
