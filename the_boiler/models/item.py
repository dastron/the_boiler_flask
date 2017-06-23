from ..webapp import database as db
from ..models.mixins import AnObject


class Item(AnObject, db.Model):
    """
    Underly model for items in the store
    """
    # __tablename__ = 'items'

    """ FROM 'AnObject MIXIN'
    title = title
    headline = Column(UnicodeText, nullable=False)
    description = Column(UnicodeText, nullable=True)

    primary_key = Column(Unicode(256), nullable=False, unique=True)
    url = Column(Unicode(2042), nullable=True)
    thumbnail = Column(Unicode(2042))

    active = Column(Boolean, default=False)

    submitted_date_time = db.Column(DateTime(timezone=True), nullable=False)
    updated_date_time = db.Column(DateTime(timezone=True), nullable=False)
    """
    price = db.Column(db.Integer, nullable=True)
    count = db.Column(db.Integer, default=1)

    @staticmethod
    def add(title, headline, description, primary_key, url, thumbnail):
        return Item(
            title=title,
            headline=headline,
            description=description,
            primary_key=primary_key,
            url=url,
            thumbnail=thumbnail)

    def insert(self):
        db.session.add(self)
        self.save()
        return self.id

    def save(self):
        db.session.commit()
