# 設定系（APIの登録とか）ひとまとめにしようとした名残、importでpythonファイルを入れればできるかなって思ってた

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

apikey = 'CHAT_API'
client = pya3rt.TalkClient(apikey)

Id = "hogehoge"