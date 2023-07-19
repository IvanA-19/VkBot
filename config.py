# Importing libraries
import vk_api
from vk_api.bot_longpoll import  VkBotLongPoll

# Api data
api_token = 'vk1.a.4Z4wBBpbMF81-8vdpxnTnd3dQq5s9GHmwk_KdNW529EmXDE4LjlwmBAfZTGB0oSmRHkjL_ccmIfruXCd1bTBTCeKbnA5E7Xu-5s5kMY0c9RYxKsZ7rJClyY1x3c4S3FWfIYsGMpL1324coeAidr1EM6hC0o-guP7b_YLQ9jwG2SEQmUBrPN2fiVwgNmkIs-fhdoIErn2mguWBHxaugWrAA'
group_id = '220483099'
group_url = 'https://vk.com/club220483099'


# Api and long poll
api = vk_api.VkApi(token=api_token)
long_poll = VkBotLongPoll(api, group_id)
