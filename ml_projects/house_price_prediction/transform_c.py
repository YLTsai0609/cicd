from typing import List
import redis
from google.cloud import bigquery

class BQ:
    def __init__(self):
        self.client = bigquery.Client(project='dbhandling')

    def query(
        self,
        sql: str,
        priority: bigquery.QueryPriority = bigquery.QueryPriority.BATCH,
    ) -> List[dict]:
        job_config = bigquery.QueryJobConfig(
            priority=priority,
        )
        query_job = self.client.query(
            query=sql,
            job_config=job_config,
        )
        result = [[row for row in rows] for rows in query_job]
        return result
    
bq = BQ()


def test_bq(bq):
    sql = 'SELECT * FROM `bigquery-public-data.covid19_aha.hospital_beds` LIMIT 1'
    rows = bq.query(sql)
    assert len(rows) >= 1
    print('we can R Bigquery!')

def test_redis():
    redis.Redis().flushall()
    k, v = 'k', 'v'
    r = redis.Redis(host='localhost',port=6379,db=0)
    r.set(k,v)
    assert r.get(k) == b'v'
    print('we can R/W Redis!')

print('some-change')
print('transform_c starts')
