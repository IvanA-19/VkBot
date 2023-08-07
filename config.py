# Importing libraries
import vk_api
from vk_api.bot_longpoll import  VkBotLongPoll

# Api data
api_token = 'YOUR API TOKEN'
group_id = 'YOUR GROUP ID'
group_url = 'YOUR GROUP URL'


# Api and long poll
api = vk_api.VkApi(token=api_token)
long_poll = VkBotLongPoll(api, group_id)
