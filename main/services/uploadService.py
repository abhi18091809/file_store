from main.DAO.fileManagementDao import *
import awsConfigurations


def upload_file_for_storage(file, option):
    if option == 's3':
        res = upload_to_s3(aws_access_key_id=awsConfigurations.aws_access_key_id,
                           aws_secret_access_key=awsConfigurations.aws_secret_access_key,
                           file=file, bucket=awsConfigurations.bucket, key=awsConfigurations.key)
    else:
        res = upload_to_filesystem(file)
    return res

# todo: make a logger for files
