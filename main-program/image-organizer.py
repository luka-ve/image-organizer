import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint


class DatabaseHandler(object):
    def __init__(self):
        with open('mongoConnectionString', 'r') as file:
            mongoConnectionString = file.read().strip()

        self.cluster = MongoClient(mongoConnectionString)
        self.db = self.cluster["image-organizer"]
        self.collection = self.db["images"]

    def add_image(self, image_entry):
        self.collection.insert_one(image_entry)

    def remove_image_by_id(self, id):
        self.collection.remove()


if __name__ == "__main__":
    db_handler = DatabaseHandler()
    db_handler.add_image({'file_path': 'C:/Users/Images/donut.jpg',
                          'tags': ['donut', 'food']})
