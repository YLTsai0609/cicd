import pytest
from bq import BQ

@pytest.fixture(scope="module")
def bq():
    bq = BQ()
    return bq


def test_bq(bq):
    sql = 'SELECT * FROM `bigquery-public-data.covid19_aha.hospital_beds` LIMIT 1'
    rows = bq.query(sql)
    assert len(rows) >= 1