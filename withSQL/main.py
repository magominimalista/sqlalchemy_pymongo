import os
from bson import ObjectId
from crud_operations import (
    connect_mongodb,
    insert_document,
    search_document,
    search_all_document,
    edit_document,
    delete_document
)

# Connect to MongoDB
collection = connect_mongodb()

if collection is not None:
    # Example document for insertion
    example_documents = [
        {
            "author": "Noah",
            "text": "Document 6",
            "tags": ["mongodb", "python3", "pymongo"]
        },
        {
            "author": "Cintia",
            "text": "Document 7",
            "tags": ["mongodb", "python3", "data"]
        },
        {
            "author": "Michele",
            "text": "Document 8",
            "tags": ["mongodb", "python3", "code"]
        },
        {
            "author": "Thiago",
            "text": "Document 9",
            "tags": ["mongodb", "python3", "query"]
        },
        {
            "author": "Winderson",
            "text": "Document 10",
            "tags": ["mongodb", "python3", "insert"]
        }
    ]

    # Insert 5 random documents
    for doc in example_documents:
        insert_document(collection, doc)

    # Insert document
    # insert_document(collection, example_document)

    # Search for documents
    print("\nSearching for documents with author 'Philipe Cairon':")
    search_document(collection, {"author": "Philipe Cairon"}, page=1, page_size=10)

    # Edit document
    # new_values = {"text": "Editando a informação."}
    # edit_document(collection, {"author": "Philipe Cairon"}, new_values)

    # Delete document
    # document_id = ObjectId("666b4dbf86396ab3b5840710")
    # delete_document(collection, {"_id": document_id})

    # Search for all documents with pagination to verify deletion
    print("\nSearching for all documents with pagination (page size 10):")
    search_all_document(collection, {})

    # Drop collection
    # collection.drop()
    # print("\nCollection 'test_collection' deleted successfully.")
