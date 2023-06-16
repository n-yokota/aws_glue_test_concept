from awsglue.context import GlueContext
from some_module import add_now_column
from pyspark.sql import functions as F
from pyspark.sql.session import SparkSession


class DataStore:
    def __init__(self, glue_context: GlueContext):
        self.gc = glue_context

    def get_some_df(self):
        self.gc.create_dynamic_frame.from_catalog(
            database="some_database",
            table_name="some_table",
        )


def calculation(data_store):
    spark_df = data_store.get_some_df()
    # 何かしらの処理
    spark_df = add_now_column(spark_df, '2020-01-01')
    return spark_df

def main(data_store: DataStore):
    spark_df = calculation(data_store)
    (
        spark_df.write.mode("overwrite")
        .format("parquet")
        .option("compression", "snappy")
        .save("s3://some_bucket/some_key")
    )

if __name__ == "__main__":
    spark = (
        SparkSession.builder
        .enableHiveSupport()
        .getOrCreate()
    )
    glue_context = GlueContext(spark.sparkContext)
    data_store = DataStore(glue_context)
    main(data_store)

