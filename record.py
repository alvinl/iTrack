import os
import redis
import time

from findi import FindMyIPhone

# Get environment variables
REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = int(os.environ["REDIS_PORT"])
REDIS_AUTH = os.environ["REDIS_AUTH"]
REDIS_DB = int(os.environ["REDIS_DB"])
APPLE_EMAIL = os.environ["APPLE_EMAIL"]
APPLE_PASSWORD = os.environ["APPLE_PASSWORD"]

# Connect to redis
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_AUTH)


iphone = FindMyIPhone(APPLE_EMAIL, APPLE_PASSWORD)

devices = [5]

for device in devices:
  iphone_location = iphone.locate(device_num=device, max_wait=20)
  latitude = iphone_location.get('latitude')
  longitude = iphone_location.get('longitude')
  location = "{'latitude': " + str(latitude) + ", 'longitude': " + str(longitude) + ", 'time': " + str(time.time()) + "}"
  r.lpush('location', location)
