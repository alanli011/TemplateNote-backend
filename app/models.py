from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


note_tags = db.Table('note_tags',
                     db.Column('note_id', db.Integer, db.ForeignKey('notes.id'), primary_key=True),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True))


# creates the users table
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)

    notebook = db.relationship('NoteBook', back_populates='user')

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
    user = db.relationship('User', back_populates='notebook')
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

    notebook = db.relationship('NoteBook', back_populates='notes')
    tags = db.relationship('Tag', secondary='note_tags', back_populates='notes')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'notebook_id': self.notebook_id,
        }


class Tag(db.Model):
    __tablename__ = 'tags'

    id = id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    notes = db.relationship('Note', secondary='note_tags', back_populates='tags')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
