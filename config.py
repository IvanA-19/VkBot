# Importing libraries
import vk_api
from vk_api.bot_longpoll import  VkBotLongPoll

# Api data
api_token = 'vk1.a.I2_QqtkHU9n0EB_mgdrcYcr_E-KZsQW59XBmRv8hB3nLmYyLRKVzL7j94unsG9qj1Eltvjm9lNJCUoU54eX2P2wp7PBh9a2P2EloR0YsRGJYG7S1mLEBLtNDTEuOPS3E_a5aNMRBeWAVCThWf2OmcTQjcfVPXx7qz4mMsauHJ4rUzwScgYSxU8q0qLGCDM6eUId_g5IOF6YJRXojKWxVFw'
group_id = '219229716'
group_url = 'https://vk.com/club219229716'

# Api and long poll
api = vk_api.VkApi(token=api_token)
long_poll = VkBotLongPoll(api, group_id)