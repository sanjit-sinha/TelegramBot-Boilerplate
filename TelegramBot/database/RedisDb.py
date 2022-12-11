import aioredis
from typing import List, Any 
from TelegramBot.config import *

redis = aioredis.from_url(REDIS_URI, decode_responses=True)

class RedisDB:
   		
	@staticmethod
	async def set(key: str, value: str) -> bool:
		"""
		Getting and setting data in redis. It take key and value argument pair as string. 
		return 'True' if the operation is successful.
		"""
		
		result = await redis.set(key, value)
		return result
		
	
	@staticmethod
	async def get(key: str) -> str:
		"""
		Take key as argument and return string value.
		( It won't return value if that key don't store string values.)	   
		"""
		
		value = await redis.get(key)
		return value
		

	@staticmethod
	async def delete(key: str ) -> bool:
		"""
		Take key as argument and delete the value from database.
		(It cane delete any type of pair including  list, set, hash )
		return 'True' if the operation is successful.
		"""
		
		value = await redis.delete(key) 
		return False if value == 0 else True
		
           	           
	@staticmethod
	async def append_list(key: str , *args: Any) -> bool:
		"""
		First argument is "key" wich take name of list as string and args take multiple values
		to append in that list.
		( values can be either string , integer, float etc. but it all will get saved in string format)
		
		Example: redisdb.list_append("my_list", 1, 2, 3)
		return 'True' if the operation is successful.
		"""
		
		try: await redis.rpush(key, *args) ; return True
		except: return False
		
		
	@staticmethod
	async def get_list(key:str ) -> List[str]:
		"""
		Take key as argument wich is name of the list.
		return value of the whole list.
		"""
		
		value = await redis.lrange(key, 0, -1)
		return value
		

	@staticmethod
	async def remove_element_from_list(key:str, value: Any, remove_all=False ) -> bool:
		"""
		Take key as first  argument wich is name of the list and
		value as second argument to remove that element from list 
		
		If remove_all is set to be True then it will delete all the matching elemnet value
		from the list.
		
		If remove_all is set to be False ( default ) then it will delete first matching element value
		from the list.
			      
		return 'True' if the operation is successfull.
		"""
		
		count = 0 if remove_all else 1
		value = await redis.lrem(key, count, value)
		return False if value == 0 else True
		
