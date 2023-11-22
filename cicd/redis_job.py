'''
redis 無法同時測試不同 function, 建議只進行整合測試
'''
import redis
import time
import fire

def job_1():
    redis.Redis().flushall()
    r = redis.Redis(host='localhost',port=6379,db=0)
    for i in range(100):
        print(f'iteration {i}')
        r.set(i, i)
        time.sleep(1)

def job_2():
    time.sleep(5)
    r = redis.Redis(host='localhost',port=6379,db=0)
    redis.Redis().flushall()
    print(r.keys())
    
fire.Fire()