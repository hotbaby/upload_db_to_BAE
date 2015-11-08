
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


def export_db(collection, *fields):
    return_filds = {}
    for filed in fields:
        return_filds[filed] = 1
    
    file_name = FILE_PATH + collection.name + ".json"
    f = open(file_name, "wb")
    cursor = collection.find().sort([("date", pymongo.DESCENDING)]).limit(MAX_RECORDS)
    while True:
        try:
            item = cursor.next()
            if item["date"]:
                item["date"] = str(item["date"])
                
            if item["_id"]:
                item["_id"] = str(item["_id"])
            f.write(json.dumps(item))
            f.write("\r\n")
        except StopIteration, e:
            print(e)
            break
        except Exception as e:
            print(e)
            break
    f.close()

if __name__ == "__main__":
    print("Connect DB.")
    connection = Connection(MONGODB_SERVER, MONGODB_PORT)
    db = connection[MONGODB_DB]
    collection_report_abstract = db[MONGODB_COLLECTION_REPORT_ABSTRACT]
    collection_report_file = db[MONGODB_COLLECTION_REPORT_FILE]
    collection_report_visited = db[MONGODB_COLLECTION_REPORT_VISITED]
    print("Export report_abstract collection.")
    export_db(collection_report_abstract, ("title", "url", "abstract", "link"))
