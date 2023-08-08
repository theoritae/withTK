from pyspark.sql import SparkSession
import os

os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /C:/git_theoritae/20230718/withTK/jitae/hadoop-aws-3.2.0.jar pyspark-shell'

spark = SparkSession.builder \
    .appName("Filtering_and_uploading_to_S3") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", "AKIA57QBQRTHKL6NULMC") \
    .config("spark.hadoop.fs.s3a.secret.key", "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") \
    .getOrCreate()

### input

s3_input_bucket = "jitae-batch-bucket-test"
s3_input_path = f"s3a://{s3_input_bucket}/"

# CSV 파일을 읽어올 경우
df = spark.read.csv(s3_input_path, header=True, inferSchema=True)

# 예시: "column_name"이 "desired_value"인 경우 필터링
filtered_df = df.filter(df["도시"] == "인천")

### output

s3_output_bucket = "jitae-batch-bucket-output-test"
s3_output_path = f"s3a://{s3_output_bucket}/"

# CSV 파일로 저장할 경우
filtered_df.write.csv(s3_output_path, header=True, mode="overwrite")

spark.stop()
