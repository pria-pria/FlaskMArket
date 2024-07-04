# Ensure you have imported your app and db correctly
from views import app, db, Item

# Create an application context
with app.app_context():
    # Create an instance of Item
    item1 = Item(name='Phone', price=500, barcode='478328783412')
    
    # Add the item to the session and commit
    db.session.add(item1)
    db.session.commit()

    # Query the database to check the item
    items = Item.query.all()
    for item in items:
        print(item.name, item.price, item.barcode)
