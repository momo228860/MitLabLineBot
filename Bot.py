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

app = Flask(__name__)

line_bot_api = LineBotApi('n0cieVD57DDKO3FCgtw9d3fLbVMoDXW1MJ6o+sVHwZ1uq6DlNtM3MdlD0EaHqagSLi0qhiQ3SrEwCId73lXb/mmOxg3as4Afg9mYRz6p5+y2lbbhMl621X2szwSjkmCmIixX5W3buZoxlP9C94rfngdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1149370c7125b2a7dd80fc47bc14852d')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
