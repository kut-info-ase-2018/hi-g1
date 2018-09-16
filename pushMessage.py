from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import VideoSendMessage
from linebot.exceptions import LineBotApiError

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

import os
import sys
import json
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

AyumuId = 'U75c52a25630767fd21c54c0277742841'
KanaId = 'Uda5dd17c887596ac407fa74fa2395696'

try:
    line_bot_api.push_message(KanaId, TextSendMessage(text='「おばけ」、「小梅ちゃん」、「自己紹介」に対応したよ？話しかけてみてね？'))
except LineBotApiError as e:
    print('You can not do this operation!')