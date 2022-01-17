# Публикуем сразу во все социальные сети

Модуль позволяет отправить изображение и текст одновременно в три социальные сети:
- Вконтакте
- Фейсбук
- Мессенджер Телеграм


# Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```
Подготовить `image` (изображение) и `message` (комментарий)


### Переменные окружения

Для корректной работы модуля необходимы следующие переменные окружения:

## ВКонтакте

```python
VK_ACCESS_TOKEN='YourVKAppAccessToken'
```
1. Создать приложение в VK.
2. По номеру приложения `client_id` используя [Implicit Flow](https://dev.vk.com/api/access-token/implicit-flow-user) получить `access_token`
3. Необходимы права `wall` и `offline`

```python
VK_PUBLIC_ID='YourVKPublicId'
```

## Telegram

Токен Вашего бота, полученный у `@BotFather`

```ython
TG_BOT_TOKEN='YourBotToken'
```
Канал Телеграм для постинга, в который добавлен Ваш бот.
```python
TG_CHANNEL='@YourTGChannel'
```

## Facebook

```python
FB_TOKEN='YOUR_APP_TOKEN'
```
1. В разделе для разработчиков создать свое приложение с типом "Другое"
2. Получить токен доступа с правами пользователя `publish_to_group`
3. Проверит работоспособность токена и наличе прав в [Graph API Explorer](https://developers.facebook.com/tools/explorer/)

```python
FB_GPOUI_ID='YOUR_FB_GROUP_ID'
```


### Пример запуска

Для запуска из командной строки необходимо передать `имя файла` с изображением и `текст` комментария для картинки
```python
python smm_reposting.py matrix.jpg 'Новая история про Избранного'
``` 

# Цель проекта

Код написан в образовательных целях на онлайн-курс для веб-разработчиков [Devman](https://dvmn.org/).