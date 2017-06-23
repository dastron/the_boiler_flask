# Import flask dependencies
from flask import Blueprint, request, render_template, redirect
from flask_login import login_required
from ..webapp import database as db


# Import the database object from the main app module
from the_boiler.models import Item
from the_boiler.mod_item.helpers import getItemID


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_items = Blueprint('items', __name__)

# View list and search items


@mod_items.route('/items/', methods=['GET', 'POST'])
@mod_items.route('/items/<int:page>/', methods=['GET', 'POST'])
def items(page=1):
    query = request.args.get('q')

    if(query is None):
        per_page = 24
        paginate = db.session.query(Item).paginate(
            page, per_page, error_out=False)
        item_exist = paginate.items
    else:
        item_exist = db.session.query(Item).filter(
            Item.title.ilike('%' + query + '%')).all()

    return render_template('item.html', items=item_exist, pagination=paginate)

# View selected item


@mod_items.route('/items/view/<id>/', methods=['GET', 'POST'])
def items_find(id):

    item_exist = getItemID(id)

    return render_template('item_view.html', item=item_exist)


@mod_items.route('/items/create/', methods=['POST'])
# @login_required
def items_create_post():
    data = request.form
    print data

    title = data['title']
    headline = data['headline']
    description = data['description']
    url = data['url']
    primary_key = data['primary_key']
    thumbnail = ''

    try:
        item_exist = Item.add(title, headline, description,
                              primary_key, url, thumbnail)
        item_id = item_exist.insert()
        return redirect("/items/" + item_id)
    except Exception as e:
        print e
        return render_template('item_create.html', error=404)


@mod_items.route('/items/create/', methods=['GET'])
# @login_required
def items_create():
    print 'outpost'
    return render_template('item_create.html')


# Delete
@mod_items.route('/items/<id>/delete', methods=['GET', 'POST'])
@login_required
def items_delete(id):

    item_exist = getItemID(id)

    db.session.delete(item_exist)
    db.session.commit()

    return redirect('/items/')
