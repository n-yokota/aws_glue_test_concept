"""
共通モジュール
"""

from pyspark.sql import functions as F

def add_now_column(df, now):
    return df.withColumn('now', F.lit(now))

