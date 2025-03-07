import requests
import math
from environs import Env


env = Env()
env.read_env()


def get_min_read_time(text: str, wpm: int = 150) -> int:
    """
    Calculate the estimated minimum reading time of an article.

    :param text: The article text.
    :param wpm: Words per minute reading speed (default is 200).
    :return: Minimum reading time in minutes (rounded up).
    """
    word_count = len(text.split())
    return math.ceil(word_count / wpm)


def send_tg_message(message, chat_id=None):
    TELEGRAM_API_KEY = env.str('TELEGRAM_API_KEY')
    CHAT_ID = env.str('CHAT_ID')

    url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={chat_id or CHAT_ID}&text={message}"
    response = requests.get(url)  # this sends the message
    return response


def get_bool_icon(bool_value):
    from django.utils.safestring import mark_safe
    if bool_value is not None:
        if bool_value:
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return mark_safe('<img src="/static/admin/img/icon-no.svg" alt="False">')
    return mark_safe('<img src="/static/admin/img/icon-unknown.svg" alt="False">')
