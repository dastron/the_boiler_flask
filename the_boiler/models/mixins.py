
from inflect import engine
from sqlalchemy import Boolean, Column, Unicode, UnicodeText
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import validates
from sqlalchemy_utils import Timestamp, Integer

inflector = engine()


class BaseEntityMixin(Timestamp):
    """The base model for every modeled entity."""

    @declared_attr
    def __tablename__(cls):
        return inflector.plural(cls.__name__.lower())

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return '<{entity_type}-{id}>'.format(
            entity_type=self.__class__, id=self.id)


class AnObject(BaseEntityMixin):
    """Anything with text and meta.

    Note: At the time, I'm not enforcing any authorship norms. Those
    are to be defined on their respective ORM classes.
    """
    title = Column(Unicode(100), nullable=False)
    headline = Column(UnicodeText, nullable=False)
    description = Column(UnicodeText, nullable=True)

    primary_key = Column(Unicode(256), nullable=False, unique=True)
    url = Column(Unicode(2042), nullable=True)
    thumbnail = Column(Unicode(2042))

    active = Column(Boolean, default=False)

    @validates('title')
    def validate_title(self, key, title):
        """Keep titles from getting too long."""
        assert len(title) >= 4 or len(
            title) <= 256, 'Must be 4 to 256 characters long.'
        return title
