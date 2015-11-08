
import pymongo
from pymongo import Connection

class NotImplement(Exception):
    pass


class DBClient(object):
    
    def __init__(self):
        pass
    
    def connect_db(self):
        raise NotImplement
    
class MongoClinet(DBClient):
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    def connect_db(self):
        self.connection = Connection(self.ip, self.port)
        return self.connection
    