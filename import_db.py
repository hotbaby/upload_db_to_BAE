
import json
import pymongo
from pymongo import Connection

MONGODB_SERVER = "192.168.199.167"
MONGODB_PORT = 27017
MONGODB_DB = "gtja"
MONGODB_COLLECTION_REPORT_ABSTRACT = "report_abstract"
MONGODB_COLLECTION_REPORT_FILE = "report_file"
MONGODB_COLLECTION_REPORT_VISITED = "report_visited"
MAX_RECORDS = 100

FILE_PATH = ""
FILE_REPORT_ABSTRACT = "report_abstract.json"

def import_db_from_file(file_name):
    with open(file_name) as f:
        pass

if __name__ == "__main__":
    print("Connect DB.")
    connection = Connection(MONGODB_SERVER, MONGODB_PORT)
    db = connection[MONGODB_DB]
    collection_report_abstract = db[MONGODB_COLLECTION_REPORT_ABSTRACT]
    collection_report_file = db[MONGODB_COLLECTION_REPORT_FILE]
    collection_report_visited = db[MONGODB_COLLECTION_REPORT_VISITED]

    print("Import DB.")
    import_db_from_file(FILE_REPORT_ABSTRACT)
    
