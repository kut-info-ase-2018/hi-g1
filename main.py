# -*- coding: utf-8 -*-
# 特定のワードに反応しつつ、それ以外はチャットAPIの会話を返答するラインボット
# 実装が必要な部分は
# 1. pushmessageするために友達追加したとき、相手のidを取得するイベント
# 2. リッチメニュー、ボタンメニュー（画像などは俺が作ってもいいからラフ考えるのがみんなでできる部分かと）
# 3. 会話型で相手の志望学群を探るなどするのなら会話の流れをもとにしたルートを作成する必要があるかなと


import os
import sys
import json

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import pya3rt

import urllib.request

import requests

# twetterと連携するための部分
# import tweepy
# from tweepy import Cursor

#APIインスタンスを作成
# Twitterの各種キーをセット
# Twi_CONSUMER_KEY = 'Twi_CONSUMER_KEY'
# Twi_CONSUMER_SECRET = 'Twi_CONSUMER_SECRET'
# Twi_ACCESS_TOKEN = 'Twi_ACCESS_TOKEN'
# Twi_ACCESS_SECRET = 'Twi_ACCESS_SECRET'
# Twi_auth = tweepy.OAuthHandler(Twi_CONSUMER_KEY, Twi_CONSUMER_SECRET)
# Twi_auth.set_access_token(Twi_ACCESS_TOKEN, Twi_ACCESS_SECRET)
# #APIインスタンスを作成
# Twi_api = tweepy.API(Twi_auth)

app = Flask(__name__)

# line-botのapi-keyとaccess_tokenを設定する場所、個人的には環境変数に設定してる
# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# チャットボットのapiを設定する場所同じく環境変数
# api関連をenvファイルにまとめてもいいかも
apikey = 'CHAT_API'
client = pya3rt.TalkClient(apikey)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 返答のイベント
@handler.add(MessageEvent, message=TextMessage)
def send_message(event):

    reply_message = client.talk(event.message.text)
    # どのようなメッセージが送られてきたかをテストするためにprintしてある。
    print(event.message.text)
    
    # event.message.textに相手から送られてきたmessageが入り、それに対応した返事を返す。if文じゃなくて辞書にしてもええんちゃうのって思う
    # 以下は俺が個人的に作ってたアイドルマスターシンデレラガールズ白坂小梅botの名残だから適当に変えて
    if (event.message.text == "おばけ") or (event.message.text == "お化け"):
        
        #line_bot_api.reply_message()で返答 
        line_bot_api.reply_message(
            #replyのイベントの際のtokenを作る
            event.reply_token,
            [
                # textに書かれたものを返答する。chr型に変換して絵文字やスタンプが選択可能。スタンプのリストなどは
                # https://developers.line.me/media/messaging-api/sticker_list.pdf
                TextSendMessage(text='あの子のこと？ふふ、あなたのことが好きみたい'),
                TextSendMessage(text=chr(0x1000A0))
            ]
        )
    elif (event.message.text == "小梅") or(event.message.text == "小梅ちゃん") or(event.message.text == "こうめちゃん"):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text='なぁに？')
            
        )
        # inで送られた文書の中にその文字が含まれているの判別も可能
    elif ("自己紹介") in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="白坂小梅…です。好きなことはホラー映画…、プロデューサーさんにも悪夢、見せてあげる" + chr(0x1000A0))
            ]
        )
    elif("大好き") in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="は、はずかしい…です。ありがとう…。")
            ]
        )
    elif("怖い")  in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="ふふっ、今度一緒にみよっか…。ホラー映画…！")
            ]
        )
    else :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message['results'][0]['reply']))


# portはherokuだと固定できないらしいのでここで指定
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)