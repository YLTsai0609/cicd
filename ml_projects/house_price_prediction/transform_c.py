from cicd.bq import BQ
import redis

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
