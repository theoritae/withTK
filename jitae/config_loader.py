import configparser
import os

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)

# kafka config
bootstrap_servers = config.get('KAFKA', 'bootstrap_servers')
topic = config.get('KAFKA', 'topic')

# s3 config
access_key = config.get('S3', 'access_key')
secret_key = config.get('S3', 'secret_key')

# s3 stream input
stream_input_bucket = config.get('S3', 'stream_input_bucket')
stream_file_name = config.get('S3', 'file_name')

# s3 batch input
batch_input_bucket = config.get('S3', 'batch_input_bucket')

# s3 batch output
batch_output_bucket = config.get('S3', 'batch_output_bucket')
batch_file_name = config.get('S3', 'batch_file_name')
