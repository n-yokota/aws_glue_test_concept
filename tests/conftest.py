import sys

import pytest
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

sys.path.append("./glue_jobs")
sys.path.append("../")


@pytest.fixture(scope="session")
def glue_context():
    """
    テスト用の高速起動の設定を使ってglue_contextを作成する
    参考:
        https://medium.com/constructor-engineering/faster-pyspark-unit-tests-1cb7dfa6bdf6
    """
    spark = (
        SparkSession.builder.master("local[1]")
        .config("spark.sql.shuffle.partitions", "1")
        .config("spark.ui.showConsoleProgress", "false")
        .config("spark.ui.enabled", "false")
        .config("spark.ui.dagGraph.retainedRootRDD", "1")
        .config("spark.ui.retainedJobs", "1")
        .config("spark.ui.retainedStages", "1")
        .config("spark.ui.retainedTasks", "1")
        .config("spark.sql. ui.retainedExecutions", "1")
        .config("spark.worker.ui.retainedExecutors", "1")
        .config("spark.worker.ui.retainedDrivers", "1")
        .getOrCreate()
    )

    yield GlueContext(spark.sparkContext)
    spark.stop()
