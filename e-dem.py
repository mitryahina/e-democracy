from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image_file = db.Column(db.String(10), unique = True, default = 'default.jpg')
    name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    education = db.Column(db.Text)
    polititics = db.Column(db.Text)
    activism = db.Column(db.Text)
    declarations = db.Column(db.Set)
    media = db.Column(db.Set)

    def __repr__(self):
        return f"Candidate('{self.image_file}', '{self.name}', '{self.birth_date}', '{self.education}', '{self.politics}'," \
               "'{self.activism}', '{self.declarations}', '{self.media}')"