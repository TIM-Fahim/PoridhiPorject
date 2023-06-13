from app import db

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    numberofexp = db.Column(db.Integer, nullable=False)
    
    def __init_(self, name, phone, numberofexp):
        self.name = name
        self.phone = phone
        self.numberofexp = numberofexp
