import os
import boto
from boto.s3.key import Key


def upload_to_s3(aws_access_key_id, aws_secret_access_key, file, bucket, key, callback=None, md5=None,
                 reduced_redundancy=False, content_type=None):
    try:
        size = os.fstat(file.fileno()).st_size
    except:
        file.seek(0, os.SEEK_END)
        size = file.tell()

    conn = boto.connect_s3(aws_access_key_id, aws_secret_access_key)
    bucket = conn.get_bucket(bucket, validate=True)
    k = Key(bucket)
    k.key = key

    if content_type:
        k.set_metadata('Content-type', content_type)

    sent = k.set_contents_from_file(file, cb=callback, md5=md5, reduced_redundancy=reduced_redundancy,
                                    rewind=True)

    file.seek(0)

    if sent == size:
        return True
    return False


def upload_to_filesystem():
    return True


def delete_file_from_s3():
    return True


def delete_file_from_filesystem():
    return True


def rename_file_in_s3():
    return True


def rename_file_in_filesystem():
    return True
