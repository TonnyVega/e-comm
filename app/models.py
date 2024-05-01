from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.Integer(), unique=True)
    created_at = db.Column(db.Date, nullable=True)
    role = db.Column(db.String(), default='users')

    __table_args__ = (
        db.CheckConstraint(role.in_(['admin', 'buyer', 'seller']), name='role_types'),
    )
    
    
    def __init__(self, username,email, phone_number, password_hash, created_at, role):
        self.username = username
        self.email = email
        self.phone_number= phone_number
        self.password_hash = password_hash
        self.created_at = datetime.utcnownow() if created_at is None else created_at
        self.role = role
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def register_user_if_not_exist(self):
        db_user = User.query.filter(User.username == self.username).all()
        if not db_user:
            db.session.add(self)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_by_username(username):
        db_user = User.query.filter(User.username == username).first()
        return db_user

    def __repr__(self):
        return f"<User {self.username}>"
