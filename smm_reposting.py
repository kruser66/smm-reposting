import os
import logging
import telegram
import vk_api as vk
from dotenv import load_dotenv
from requests import (
    ReadTimeout,
    ConnectTimeout,
    HTTPError,
    Timeout,
    ConnectionError
)


logger = logging.getLogger('smm_logger')


def post_to_telegram_channel(bot, channel_id, filename, message):

    with open(filename, 'rb') as file:
        bot.send_photo(chat_id=channel_id, photo=file, caption=message)
    # bot.send_message(chat_id=channel_id, text=message)


if __name__ == '__main__':

    load_dotenv()
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = int(os.getenv('VK_PUBLIC_ID'))

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_channel = os.getenv('TG_CHANNEL')

    bot = telegram.Bot(token=tg_bot_token)

    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    filename = 'images/matrix.jpg'
    message = '''В двух реальностях Нео снова придется
выбирать, следовать ли за белым кроликом.
Выбор, пусть и иллюзорный, все еще
остается единственным путем в Матрицу
или из нее, что более опасно, чем когда-либо.
'''

    try:
        post_to_telegram_channel(bot, tg_channel, filename, message)
    except (
        ReadTimeout,
        ConnectTimeout,
        HTTPError,
        Timeout,
        ConnectionError
    ) as error:
        logger.exception(f'Ошибка в запросе: {error}')
