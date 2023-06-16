from sample_batch_script import (
    DataStore,
    calculation,
)


class MockDataStore(DataStore):
    def get_some_df(self):
        return self.gc.spark_session.createDataFrame(
            [
                [1, "test1"],
                [2, "test2"],
            ],
            [
                "a",
                "b",
            ],
        )


def test_calculation(glue_context):
    """
    組織階層が登録されていない法人は登録されていないことを確認
    """
    ds = MockDataStore(glue_context)
    result_df = calculation(ds)
    csv = result_df.toPandas().to_csv(index=False)
    print(csv)
    assert (
        csv.strip()
        == """
a,b,now
1,test1,2020-01-01
2,test2,2020-01-01
    """.strip()
    )
