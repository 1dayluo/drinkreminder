import os

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
YAML_PATH = CURRENT_PATH + '/config.yaml'
SEND_T = {
    "touser":"{}",
    "template_id":"{}",
	"url":"https://www.bilibili.com/video/BV1j34y1d7hL",
    "topcolor":"#FF0000",
    "data":{
            "title": {
                "value":"(盯)记得:",
                "color":"#3399ff"
            },
            "content":{
                "value":"喝水啦!!",
                "color":"#ff1a1a"
            },
            "meow":{
                "value":"（￣▽￣）～■□～（￣▽￣） 这是今天第: {} 杯",
                "color":"#173177"
            }
    }
}
TPL_ID = "" #模板id
APIID = ""
APISECRET = ""
USER_LIST = [] # 要发送的用户id