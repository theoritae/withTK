from pyspark.sql import SparkSession
import config_loader

spark = SparkSession.builder.appName("Filtering_and_uploading_to_S3").getOrCreate()

### input

s3_input_bucket = config_loader.stream_input_bucket
s3_input_path = "s3://{}/path/to/input/folder".format(s3_input_bucket)

# CSV 파일을 읽어올 경우
df = spark.read.csv(s3_input_path, header=True, inferSchema=True)

# 예시: "column_name"이 "desired_value"인 경우 필터링
filtered_df = df.filter(df["column_name"] == "desired_value")



### output

s3_output_bucket = "your_output_bucket"
s3_output_path = "s3://{}/path/to/output/folder".format(s3_output_bucket)

# CSV 파일로 저장할 경우
filtered_df.write.csv(s3_output_path, header=True, mode="overwrite")

spark.stop()
