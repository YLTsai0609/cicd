import pytest
import redis

def test_redis():
    redis.Redis().flushall()
    k, v = 'k', 'v'
    r = redis.Redis(host='localhost',port=6379,db=0)
    r.set(k,v)
    assert r.get(k) == b'v'