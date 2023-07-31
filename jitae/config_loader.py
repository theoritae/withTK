import configparser
import os

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)

bootstrap_servers = config.get('KAFKA', 'bootstrap_servers')
topic = config.get('KAFKA', 'topic')
access_key = config.get('S3', 'access_key')
secret_key = config.get('S3', 'secret_key')
bucket_name = config.get('S3', 'bucket_name')
file_name = config.get('S3', 'file_name')
