from the_boiler.models import Item
from the_boiler.webapp import database as db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound


def getItemID(primary_key):
    try:
        item_exist = db.session.query(Item).filter(
            Item.primary_key == primary_key).one()

    except MultipleResultsFound, e:
        print e

    except NoResultFound, e:
        print 'no user, create one'

    return item_exist
