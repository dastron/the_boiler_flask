from ..webapp import database as db
from ..models.mixins import BaseEntityMixin
from sqlalchemy import Unicode, Boolean


class User(BaseEntityMixin, db.Model):
    """
    Underly model for the user
    """
    # __tablename__ = 'users'

    name = db.Column(Unicode(2042), nullable=False)
    image_url = db.Column(Unicode(256), nullable=True)
    email = db.Column(Unicode(256), nullable=True)
    token = db.Column(Unicode(256), nullable=True)
    authenticated = db.Column(Boolean, default=True)

    # submitted_date_time = db.Column(DateTime(timezone=True), nullable=False)
    # updated_date_time = db.Column(DateTime(timezone=True), nullable=False)

    @staticmethod
    def add(name, image_url, email):
        return User(name=name, image_url=image_url, email=email)

    def insert(self):
        db.session.add(self)
        self.save()
        return self.id

    def save(self):
        db.session.commit()

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
