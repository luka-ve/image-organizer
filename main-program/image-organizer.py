import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint


class DatabaseHandler(object):
    def __init__(self):
        with open('mongoConnectionString', 'r') as file:
            mongoConnectionString = file.read().strip()

        self.cluster = MongoClient(mongoConnectionString)
        self.db = self.cluster['image-organizer']
        self.collection = self.db['images']

    def add_entry(self, entry):
        self.collection.insert_one(entry)

    def remove_image_by_id(self, id):
        self.collection.remove()


def main():
    db_handler = DatabaseHandler()
    results = db_handler.collection.find({'tags': 'picture'})

    for result in results:
        print(result['file_path'])


if __name__ == '__main__':
    main()
