"""
Basic class structure for using and helping out with redis database.
Although this repository uses mongodb instead of redis.
"""

import aioredis
from typing import List, Any
from TelegramBot.config import *

REDIS_URI = "redis://default:BO44Y0Dim3FkS74Q10WB@containers-us-west-163.railway.app:6825"  # (URI_EXAMPLE)
redis = aioredis.from_url(REDIS_URI, decode_responses=True)


class RedisDB:

    @staticmethod
    async def set(key: str, value: str) -> bool:
        """Getting and setting data in redis. It takes key and value pair argument as string.
        return 'True' if the operation is successful."""

        return await redis.set(key, value)

    @staticmethod
    async def get(key: str) -> str:
        """
		Take key as argument and return string value.
		(It won't return value if that key don't store string class values.)	   
		"""

        return await redis.get(key)

    @staticmethod
    async def delete(key: str) -> bool:
        """
		Take key as argument and delete the value from database.
		(It can delete any type of key, value pair including  list, set, hash )
		return 'True' if the operation is successful.
		"""

        value = await redis.delete(key)
        return value != 0

    @staticmethod
    async def append_list(key: str, *args: Any) -> bool:
        """
		First argument is "key" which take name of list as string and args take multiple values
		to append in that list.
		( values can be either string , integer, float etc. but it all will get saved in string format)
		
		Example: redisdb.append_list("my_list", 1, 2, 3)
		return 'True' if the operation is successful.
		"""

        try:
            await redis.rpush(key, *args);
            return True
        except:
            return False

    @staticmethod
    async def get_list(key: str) -> List[str]:
        """
		Take key as argument which is name of the list.
		return value of the whole list.
		"""

        return await redis.lrange(key, 0, -1)

    @staticmethod
    async def remove_element_from_list(key: str, value: Any, remove_all=False) -> bool:
        """
		Take key as first  argument which is name of the list and
		value as second argument to remove that element from list 
		
		If remove_all is set to be True then it will delete all the matching element value
		from the list.
		
		If remove_all is set to be False ( default ) then it will delete first matching element value
		from the list.

		return 'True' if the operation is successful.
		"""

        count = 0 if remove_all else 1
        value = await redis.lrem(key, count, value)
        return value != 0
