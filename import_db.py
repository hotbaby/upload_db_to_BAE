#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from win32con import FILE_NAME_OPENED
reload(sys)
sys.setdefaultencoding( "utf-8" )

import json
from pymongo import MongoClient
import conf
import bos_conf
from baidubce.services.bos.bos_client import BosClient

bos_client = BosClient(bos_conf.config)

def download_file_from_bae(bucket_name, object_name, file_name):
    bos_client.get_object_to_file(bucket_name, object_name, file_name)

def import_db_from_file(collection, file_name):
    with open(file_name) as f:
        for line in f:
            item = json.loads(line)
            if collection.find_one({"url":item["url"]}) != None:
                continue
            
            if item.has_key("_id") == True:
                item.pop("_id")
            collection.insert(item)

def import_db():
    print("Connect DB.")
    connection = MongoClient(conf.MONGODB_SERVER, conf.MONGODB_PORT)
    db = connection[conf.MONGODB_DB]
    collection_report_abstract = db[conf.MONGODB_COLLECTION_REPORT_ABSTRACT]
    collection_report_file = db[conf.MONGODB_COLLECTION_REPORT_FILE]
    collection_report_visited = db[conf.MONGODB_COLLECTION_REPORT_VISITED]

    print("Import DB.")
    collection = db["test"]
    
    bucket_name = conf.BUCKET_NAME
    object_name = conf.OBJECT_REPORT_ABSTRACT
    file_name = conf.FILE_PATH + object_name
    download_file_from_bae(bucket_name, object_name, file_name)
    import_db_from_file(collection, file_name)
    
    object_name = conf.OBJECT_REPORT_FILE
    file_name = conf.FILE_PATH + object_name
    download_file_from_bae(bucket_name, object_name, file_name)
    import_db_from_file(collection, file_name)
    print("Import successfully")
    
def test(file_name):
    print(file_name)
    f = open(file_name)
    s = f.read(1024*1024)
    s_json = json.loads(s)
    for item in s_json:
        print(json.dumps(item))
    f.close()

if __name__ == "__main__":
    file_name = conf.FILE_PATH + conf.MONGODB_COLLECTION_REPORT_ABSTRACT
    test(file_name)
