import bos_conf
import conf

from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient

bos_client = BosClient(bos_conf.config)

bucket_name = "database"
object_key = conf.MONGODB_COLLECTION_REPORT_ABSTRACT + ".json"
file_name = conf.FILE_PATH + conf.MONGODB_COLLECTION_REPORT_ABSTRACT + ".json"
bos_client.put_object_from_file(bucket_name, object_key, file_name)

object_key = conf.MONGODB_COLLECTION_REPORT_FILE + ".json"
file_name = conf.FILE_PATH + conf.MONGODB_COLLECTION_REPORT_FILE + ".json"
bos_client.put_object_from_file(bucket_name, object_key, file_name)