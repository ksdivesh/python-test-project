from config.db import cursor, db

class Item:

    def __init__(self, item_id = None, category_id = None, item_name = None, item_price = None, created_on = None, updated_on = None):
        self.item_id = item_id
        self.category_id = category_id
        self.item_name = item_name
        self.item_price = item_price
        self.created_on = created_on
        self.updated_on = updated_on


    def insert(self):
        sql = "INSERT INTO items (category_id, item_name, item_price) VALUES('{}', '{}', '{}')".format(self.category_id, self.item_name, self.item_price)
        cursor.execute(sql)
        self.item_id = cursor.lastrowid
        db.commit()






