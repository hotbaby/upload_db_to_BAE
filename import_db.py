#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import json
import pymongo
from pymongo import MongoClient
import conf

def import_db_from_file(collection, file_name):
    with open(file_name) as f:
        for line in f:
            item = json.loads(line)
            if collection.find_one({"url":item["url"]}) != None:
                continue
            
            if item.has_key("_id") == True:
                item.pop("_id")
            collection.insert(item)

if __name__ == "__main__":
    print("Connect DB.")
    connection = MongoClient(conf.MONGODB_SERVER, conf.MONGODB_PORT)
    db = connection[conf.MONGODB_DB]
    collection_report_abstract = db[conf.MONGODB_COLLECTION_REPORT_ABSTRACT]
    collection_report_file = db[conf.MONGODB_COLLECTION_REPORT_FILE]
    collection_report_visited = db[conf.MONGODB_COLLECTION_REPORT_VISITED]

    print("Import DB.")
    collection = db["test"]
    file_name = conf.FILE_PATH + collection_report_abstract.name + ".json"
    import_db_from_file(collection, file_name)
    file_name = conf.FILE_PATH + collection_report_file.name + ".json"
    import_db_from_file(collection, file_name)
    print("Import successfully")
    
