# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32304
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        self.modified_count = 0

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary    
            print("TRUE: Document created.")
        else:
            print("FALSE: Faild to create document")
           
# Create method to implement the R in CRUD.
    def readMany(self, query):
        cursor = self.collection.find(query) #creating cursor and querying dataase collection. using find and query variable to filter results.
        listResult = list(cursor) #Converting results to a list.
        return listResult
    
    def readOne(self, query):
        result = self.collection.find_one(query)
        return result
        
# Update Method
    def update(self, query, update_data):
        
        if query and update_data:
            result = self.collection.update_many(query, {'$set' : update_data})
            self.modified_count += result.modified_count
            return result.modified_count
        else:
            raise Exception("Invalid input.")
# Delete Method
    def delete(self, query):
        if query:
            result = self.collection.delete_many(query)
            print(f"{result.deleted_count} documents deleted.")
        else:
            raise Exception("Invalid input.")