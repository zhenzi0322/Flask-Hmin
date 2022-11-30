from redis import StrictRedis


redis = StrictRedis(host='localhost', port=6379, db=0, password='')
a = redis.setex('name', value="demo".encode('utf8'), time=10)
print(a)
print(redis.get('name'))
print(redis.exists("name"))