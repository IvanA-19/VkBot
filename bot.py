# Importing libraries
from config import *
from db_handler import check_member, add_member, remove_member
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# Sending message via bot
def write_message(send_id: int, message: str, keyboard=None) -> None:
    data = {'peer_id': send_id, 'message': message, 'random_id': get_random_id()}
    if keyboard is not None:
        data['keyboard'] = keyboard.get_keyboard()
    api.method('messages.send', data)


# Main circle
def run_api() -> None:
    for event in long_poll.listen():
        # Answering on message from user
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'].lower() == 'Hello'.lower():
                write_message(event.obj.message['peer_id'], "Hello! Welcome to our group!")
            elif "База знаний".lower() in event.obj.message['text'].lower():
                if check_member(event.obj.message['from_id']):
                    write_message(event.obj.message['peer_id'], "Спасибо, за подписку! Высылаю базу знаний!")
                else:
                    write_message(event.obj.message['peer_id'],
                                  f"Для использования всех функций подпишитесь на группу!\n{group_url}")
            elif event.obj.message['text'].lower() == 'Start'.lower():
                keyboard = VkKeyboard()
                keyboard.add_button("База знаний", VkKeyboardColor.POSITIVE)
                write_message(event.obj.message['peer_id'], "Рад приветствовать!", keyboard)
            else:
                write_message(event.obj.message['peer_id'], "Sorry I don't understand. Write start.")

        # Checking following of new user
        elif event.type == VkBotEventType.GROUP_JOIN:
            write_message(event.obj.user_id, "Thanks for following!\nEnjoy your use!")
            add_member(event.obj.user_id)
        elif event.type == VkBotEventType.GROUP_LEAVE:
            write_message(event.obj.user_id, "Было приятно с вами работать! Всего доброго!")
            remove_member(event.obj.user_id)
