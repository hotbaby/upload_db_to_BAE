import bos_conf
import conf

from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient

bos_client = BosClient(bos_conf.config)

bucket_name = conf.BUCKET_NAME
object_key = conf.OBJECT_REPORT_ABSTRACT
file_name = conf.FILE_PATH + conf.MONGODB_COLLECTION_REPORT_ABSTRACT
bos_client.put_object_from_file(bucket_name, object_key, file_name)
print("Upload %s successfully. " % file_name)

object_key = conf.OBJECT_REPORT_FILE
file_name = conf.FILE_PATH + conf.MONGODB_COLLECTION_REPORT_FILE
bos_client.put_object_from_file(bucket_name, object_key, file_name)
print("Upload %s successfully. " % file_name)