import os
import logging
import telegram
import requests
import argparse
import vk_api as vk
from dotenv import load_dotenv


logger = logging.getLogger('smm_logger')


def post_telegram(bot, channel_id, filename, message):

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


def post_vkontakte(vk_api, vk_upload, group_id, filename, message):
    photo = upload_photo_wall(vk_upload, filename, group_id)
    vk_api.wall.post(
        owner_id=-group_id,
        message=message,
        attachments=photo
    )


def post_facebook(fb_api_url, fb_token, fb_group_id, filename, message):
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


def create_parser():
    parser = argparse.ArgumentParser(
        description='Определяем победителя конкурса в Инстаграмм'
    )
    parser.add_argument(
        'image',
        nargs='+',
        help='Файл с картинкой для поста'
    )
    parser.add_argument('text', nargs='+', help='Текст для поста')

    return parser


if __name__ == '__main__':

    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    parser = create_parser()
    args = parser.parse_args()

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
    fb_group_id = os.getenv('FB_GPOUP_ID')
    fb_api_url = ' https://graph.facebook.com/v12.0/'

    filename = args.image[0]
    message = args.text[0]

    print(args)
    print(filename, message)

    if os.path.exists(filename):
        post_telegram(bot, tg_channel, filename, message)
        post_vkontakte(vk_api, vk_upload, vk_group_id, filename, message)
        post_facebook(fb_api_url, fb_token, fb_group_id, filename, message)
    else:
        logger.error(f'Файл {filename} не существует. Проверьте параметры!')
