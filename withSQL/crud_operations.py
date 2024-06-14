from datetime import datetime
import pymongo as pyM
import os


# Function to connect to MongoDB
def connect_mongodb():
    mongo_uri = os.getenv("MONGO_URL", "mongodb+srv://lipe:#P0rtug4l@tester.sdz6jbb.mongodb.net/")
    try:
        client = pyM.MongoClient(mongo_uri)
        db = client.test
        collection = db.test_collection
        print("Collection selected:", db.test_collection)
        return collection
    except pyM.errors.ConnectionError as ce:
        print("Connection error:", ce)
    except pyM.errors.PyMongoError as pe:
        print("Pymongo error:", pe)
    except Exception as e:
        print("Other error occurred:", e)
        return None


# Function to insert a document
def insert_document(collection, document):
    try:
        document['date'] = datetime.utcnow()
        post_id = collection.insert_one(document).inserted_id
        print("Inserted document ID:", post_id)
    except pyM.errors.PyMongoError as err:
        print("Error inserting document:", err)


# Function to search for documents
def search_document(collection, query, page=1, page_size=10):
    try:
        skips = page_size * (page - 1)
        documents = collection.find(query).skip(skips).limit(page_size)
        for doc in documents:
            print(doc)
    except pyM.errors.PyMongoError as err:
        print("Error searching for documents:", err)


# Function to search for documents with pagination
def search_all_document(collection, query, page_size=10):
    try:
        page = 0
        while True:
            skips = page_size * page
            documents = collection.find(query).skip(skips).limit(page_size)
            docs_list = list(documents)
            if not docs_list:
                break
            for doc in docs_list:
                print(doc)
            page += 1
    except pyM.errors.PyMongoError as err:
        print("Error searching for documents:", err)


# Function to edit a document
def edit_document(collection, query, new_values):
    try:
        result = collection.update_one(query, {'$set': new_values})
        if result.matched_count > 0:
            print("Document updated successfully.")
        else:
            print("No documents match the given query.")
    except pyM.errors.PyMongoError as err:
        print("Error updating document:", err)


# Function to delete a document
def delete_document(collection, query):
    try:
        result = collection.delete_one(query)
        if result.deleted_count > 0:
            print("Document successfully deleted.")
        else:
            print("No documents match the given query.")
    except pyM.errors.PyMongoError as err:
        print("Error deleting document:", err)
