# Importing libraries
from config import *
from db_handler import check_member, add_member, remove_member
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id


# Sending message via bot
def write_message(send_id: int, message: str) -> None:
    api.method('messages.send', {'peer_id': send_id, 'message': message, 'random_id': get_random_id()})


# Main circle
def run_api() -> None:
    for event in long_poll.listen():
        # Answering on message from user
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'] == 'Hello':
                write_message(event.obj.message['peer_id'], "Hello! Welcome to our group!")
            elif event.obj.message['text'] == 'База знаний':
                if check_member(event.obj.message['from_id']):
                    write_message(event.obj.message['peer_id'], "Спасибо, за подписку! Высылаю базу знаний!")
                else:
                    write_message(event.obj.message['peer_id'],
                                  f"Для использования всех функций подпишитесь на группу!\n{group_url}")
            else:
                write_message(event.obj.message['peer_id'], "Sorry! I don't understand...")

        # Checking following of new user
        elif event.type == VkBotEventType.GROUP_JOIN:
            write_message(event.obj.user_id, "Thanks for following!\nEnjoy your use!")
            add_member(event.obj.user_id)
        elif event.type == VkBotEventType.GROUP_LEAVE:
            write_message(event.obj.user_id, "Было приятно с вами работать! Всего доброго!")
            remove_member(event.obj.user_id)
