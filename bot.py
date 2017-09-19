from flask import Flask, request, make_response
from googleapiclient.discovery import build
import os
from pprint import pprint
import sys
import telebot
from telebot import types


if (len(sys.argv) > 1):
    # Debug
    POLLING = True
else:
    # Production
    POLLING = False
    WEBHOOK_URL = "https://google-image-search-telegram.herokuapp.com"

BOT_NAME = "g_imagebot"
CSE_KEY = "AIzaSyAgaWiuUSMyx2rpXNCM7cjqj70g4uJpHPg"
CSE_CX = "017839625266631737468:49zyrnlnquw"
API_TOKEN = "433849602:AAHYvB5-EzsWp7-tiOD9yBRY6jffZxxoGIw"
BATCH = 10

server = Flask(__name__)
bot = telebot.TeleBot(API_TOKEN)

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, searchType='image', **kwargs).execute()
    imgs = []
    if 'items' not in res:
        return False
    for item in res['items']:
        imgs.append((item['link'], item['image']['thumbnailLink']))
    return imgs

@bot.inline_handler(lambda query: True)
def default_query(inline_query):
    if (inline_query.query == ''):
        return

    if inline_query.offset == '':
        offset = 0
    else:
        offset = int(inline_query.offset)

    search_term = inline_query.query
    search_results = google_search(search_term, CSE_KEY, CSE_CX, safe="off", num=BATCH, start=(offset * BATCH) + 1)

    rs = []
    if not search_results:
        rs.append(types.InlineQueryResultPhoto("1", "https://images-na.ssl-images-amazon.com/images/I/41q1QAln%2BQL._AC_UL320_SR248,320_.jpg", "https://images-na.ssl-images-amazon.com/images/I/41q1QAln%2BQL._AC_UL320_SR248,320_.jpg"))
    else:
        try:
            id = 0
            for each in search_results:
                id += 1
                rs.append(types.InlineQueryResultPhoto(str(id), each[0], each[1]))
        except Exception as e:
            print(e)
    
    bot.answer_inline_query(inline_query.id, rs, cache_time=2592000, next_offset=offset + 1)


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    webhook = bot.get_webhook_info()
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + "/bot")
    return "!", 200


if (POLLING):
    bot.remove_webhook()
    bot.polling()
else:
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
