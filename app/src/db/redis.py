import os

import redis
from db.cache import AbstractCache

redis_host = os.getenv("AUTH_POSTGRES_USER")
redis_port = os.getenv("AUTH_POSTGRES_USER")


# class RedisCache(AbstractCache):
#     def __init__(self):
#         self.r = redis.Redis(host='localhost', port=6379, db=0)
#
#     def get_cache(self, id_: str):
#         data = self.r.get(id_)
#         if not data:
#             return None
#         return data
#
#     def put_data_to_cache(self, id_: str, user_agent: str, data: str):
#         self.r.set(id_ + user_agent, data)
#
#     def delete_cache(self, id_: str):
#         self.r.delete(id_)


jwt_redis_blocklist = redis.Redis(
    host="localhost", port=6379, db=1, decode_responses=True
)
