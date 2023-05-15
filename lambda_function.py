import json
import os
import shutil
import subprocess
import boto3
from datetime import datetime

s3 = boto3.client('s3')

directory_prefix = os.getenv('ZIP_FILENAME', 'mongodb_backup')
s3_bucket = os.getenv('S3_BUCKET')
connection_string = os.getenv('MONGODB_URI')
_utc_time = datetime.utcnow().isoformat(timespec='milliseconds')
directory_name = f"{directory_prefix}-{_utc_time}"


def lambda_handler(event, context):
    _status_code, _response = 200, f'Uploaded to {s3_bucket}/{directory_name}.zip'

    try:
        subprocess.run(["./mongodump", "--uri", connection_string, "--out", f"/tmp/{directory_name}"])
        shutil.make_archive(f'/tmp/{directory_name}', 'zip', f'/tmp/{directory_name}')
        s3.upload_file(f"/tmp/{directory_name}.zip", s3_bucket, f"{directory_name}.zip")
    except Exception as e:
        _status_code, _response = 400, str(e)

    return {
        'statusCode': _status_code,
        'body': json.dumps(_response)
    }
