# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymongo

class MongoPipeline(object):
    collection_name = 'films'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['rotten_tomatoes_db']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print("Inserting item into MongoDB:", item)
        self.db[self.collection_name].insert_one(dict(item))
        return item

