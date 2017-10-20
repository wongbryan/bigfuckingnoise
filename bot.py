import datetime
from authentication import api

message = "The time is {}. Do you know where your twitter bot is?".format(
    datetime.datetime.now().strftime('%-I:%m %p'))
print('posting this clever message to twitter:')
print(message)

api.update_status(message)

print('success!')
