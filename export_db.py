
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import json
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import conf

def export_db(collection, *fields):
    return_filds = {}
    for filed in fields:
        return_filds[filed] = 1
    
    file_name = conf.FILE_PATH + collection.name
    f = open(file_name, "wb")
    cursor = collection.find().sort([("create_date", pymongo.DESCENDING)]).limit(conf.MAX_RECORDS)
    while True:
        try:
            item = cursor.next()

            now = datetime.now()
            time_delta = now - item["create_date"]
            if time_delta.days >= conf.EXPIRE_DAYS:
                break
            
            for k in item.keys():
                if isinstance(item[k], (datetime, ObjectId)):
                    item[k] = str(item[k])
                
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
    connection = MongoClient(conf.MONGODB_SERVER, conf.MONGODB_PORT)
    db = connection[conf.MONGODB_DB]
    collection_report_abstract = db[conf.MONGODB_COLLECTION_REPORT_ABSTRACT]
    collection_report_file = db[conf.MONGODB_COLLECTION_REPORT_FILE]
    
    print("Export DB.")
    print("Export %s." % collection_report_abstract.name)
    export_db(collection_report_abstract)
    print("Export %s." % collection_report_file.name)
    export_db(collection_report_file)
    print("Export successfully.")
