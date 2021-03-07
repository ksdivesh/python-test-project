from config.db import cursor, db

class ItemCategory:

    def __init__(self, category_id = None, category_name = None, created_on = None, updated_on = None):
        self.category_id = category_id
        self.category_name = category_name
        self.created_on = created_on
        self.updated_on = updated_on

    def get(self):
        sql = "SELECT * FROM items_categories"
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        return result

    def info(self):
        sql = "SELECT * FROM items_categories WHERE category_id = '{}'".format(self.category_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        db.commit()
        return result


    def insert(self):
        sql = "INSERT INTO items_categories (category_name) VALUES('{}')".format(self.category_name)
        cursor.execute(sql)
        self.category_id = cursor.lastrowid
        db.commit()

    def update(self):
        sql = "UPDATE item_categories SET category_name = '{}' WHERE category_id = '{}'".format(self.category_name, self.category_id)
        cursor.execute(sql)
        db.commit()

    def delete(self):
        sql = "DELETE FROM item_categories WHERE category_id = '{}'".format(self.category_id)
        cursor.execute(sql)
        db.commit()





