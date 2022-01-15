# Публикуем сразу во все социальные сети

Модуль позволяет отправить изображение и текст одновременно в три социальные сети:
- Вконтакте
- Фейсбук
- Мессенджер Телеграм


# Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```Python
pip install -r requirements.txt
```
Подготовить `image` (изображение) и `message` (комментарий)


### Переменные окружения

Для корректной работы модуля необходимы следующие переменные окружения:

## ВКонтакте

```Python
VK_ACCESS_TOKEN='YourVKAppAccessToken'
```
1. Создать приложение в VK.
2. По номеру приложения `client_id` используя [Implicit Flow](https://dev.vk.com/api/access-token/implicit-flow-user) получить `access_token`
3. Необходимы права `wall` и `offline`

```Python
VK_PUBLIC_ID='YourVKPublicId'
```

## Telegram

Токен Вашего бота, полученный у `@BotFather`

```Python
TG_BOT_TOKEN='YourBotToken'
```
Канал Телеграм для постинга, в который добавлен Ваш бот.
```Python
TG_CHANNEL='@YourTGChannel'
```

## Facebook

```Python
FB_TOKEN='YOUR_APP_TOKEN'
```
1. В разделе для разработчиков создать свое приложение с типом "Другое"
2. Получить токен доступа с правами пользователя `publish_to_group`
3. Проверит работоспособность токена и наличе прав в [Graph API Explorer](https://developers.facebook.com/tools/explorer/)

```Pyton
FB_GPOUI_ID='YOUR_FB_GROUP_ID'
```


### Пример запуска

```
python smm_reposting.py
``` 

# Цель проекта

Код написан в образовательных целях на онлайн-курс для веб-разработчиков [Devman](https://dvmn.org/).