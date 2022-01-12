import os
import logging
import telegram
import requests
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


def upload_photo_wall(vk_upload, filename, group_id):
    photo = vk_upload.photo_wall(
        photos=filename,
        group_id=group_id
    )
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']

    vk_photo_url = f'photo{owner_id}_{photo_id}'

    return vk_photo_url


def post_to_vk_public(vk_api, vk_upload, group_id, filename, message):
    photo = upload_photo_wall(vk_upload, filename, group_id)
    vk_api.wall.post(
        owner_id=-group_id,
        message=message,
        attachments=photo
    )


def post_to_fb_group(fb_api_url, fb_token, fb_group_id, filename, message):
    api_photo_url = f'{fb_api_url}{fb_group_id}/photos'

    data = {
        'access_token': fb_token,
        'caption': message,
    }
    with open(filename, 'rb') as file:
        files = {
            'media': file
        }
        response = requests.post(api_photo_url, data=data, files=files)
    response.raise_for_status()

    return response


if __name__ == '__main__':

    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    load_dotenv()

    # VKontakte
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = int(os.getenv('VK_PUBLIC_ID'))

    vk_session = vk.VkApi(token=vk_access_token, api_version='5.131')
    vk_upload = vk.VkUpload(vk_session)
    vk_api = vk_session.get_api()

    # Telegram
    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_channel = os.getenv('TG_CHANNEL')
    bot = telegram.Bot(token=tg_bot_token)

    # Facebook
    fb_token = os.getenv('FB_TOKEN')
    fb_group_id = os.getenv('FB_GPOUI_ID')
    fb_api_url = ' https://graph.facebook.com/v12.0/'

    filename = 'images/matrix.jpg'
    message = '''В двух реальностях Нео снова придется
выбирать, следовать ли за белым кроликом.
Выбор, пусть и иллюзорный, все еще
остается единственным путем в Матрицу
или из нее, что более опасно, чем когда-либо.
'''

    try:
        post_to_telegram_channel(bot, tg_channel, filename, message)
        post_to_vk_public(vk_api, vk_upload, vk_group_id, filename, message)
        post_to_fb_group(fb_api_url, fb_token, fb_group_id, filename, message)
    except (
        ReadTimeout,
        ConnectTimeout,
        HTTPError,
        Timeout,
        ConnectionError
    ) as error:
        logger.exception(f'Ошибка в запросе: {error}')
