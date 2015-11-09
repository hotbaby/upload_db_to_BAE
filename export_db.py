
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import json
import pymongo
from pymongo import Connection
import conf

def export_db(collection, *fields):
    return_filds = {}
    for filed in fields:
        return_filds[filed] = 1
    
    file_name = conf.FILE_PATH + collection.name + ".json"
    f = open(file_name, "wb")
    cursor = collection.find().sort([("date", pymongo.DESCENDING)]).limit(conf.MAX_RECORDS)
    while True:
        try:
            item = cursor.next()
            if item["date"]:
                item["date"] = str(item["date"])
                
            if item["_id"]:
                item["_id"] = str(item["_id"])
            f.write(json.dumps(item))
            f.write("\n")
        except StopIteration, e:
            print(e)
            break
        except Exception as e:
            print(e)
            break
    f.close()

if __name__ == "__main__":
    print("Connect DB.")
    connection = Connection(conf.MONGODB_SERVER, conf.MONGODB_PORT)
    db = connection[conf.MONGODB_DB]
    collection_report_abstract = db[conf.MONGODB_COLLECTION_REPORT_ABSTRACT]
    collection_report_file = db[conf.MONGODB_COLLECTION_REPORT_FILE]
    
    print("Export DB.")
    export_db(collection_report_abstract)
    export_db(collection_report_file)
    print("Export successfully.")