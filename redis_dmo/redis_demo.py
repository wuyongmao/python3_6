import redis
r = redis.Redis(host='192.168.2.130', port=6379)
# r = redis.StrictRedis(host='0.0.0.0', port=6379)
# 如果要指定数据库，则 r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0)
r.set('name', 'test')
print(r.get('name'))
# 输出结果
 
pool = redis.ConnectionPool(host='192.168.2.130', port=6379)
r = redis.StrictRedis(connection_pool=pool)
# r = redis.Redis(connection_pool=pool)
r.set('age', '16')
print(r.get('age'))