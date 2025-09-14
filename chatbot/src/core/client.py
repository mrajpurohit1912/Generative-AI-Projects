import asyncio
from redis.asyncio import Redis
import json

_redi_client = None

def get_redis_client():
    if _redi_client is None:
        redis_client = Redis(decode_responses=True)
        return  redis_client
    return redis_client
# my_dict = {'name':'mahavir',
#            'age':26}

# async def main():
#     response = await redis_client.hset('mahavir',key="email_id",value="abc@gmail.com")
#     print(response)
# if __name__ == "__main__":
#     asyncio.run(main())
