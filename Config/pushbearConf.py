# -*- coding: utf8 -*-
import logging.handlers
import time
import os
from conf import _get_yaml
import sys
sys.path.append("..")
import myUrllib.HttpClient as HttpClient
from myUrllib.HttpClient import WX_HTTPClient


PUSH_BEAR_API_PATH = "https://pushbear.ftqq.com/sub"
_logger = logging.getLogger("daily")

Pushbear= {  # push通知
        "req_url": "/sub",
        "req_type": "post",
        "Referer": "",
        "Content-Type": 1,
        "Host": "pushbear.ftqq.com",
        "re_try": 10,
        "re_time": 0.01,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": True,
    }

def sendPushBear(msg):
    """
    pushBear微信通知
    :param str: 通知内容 content
    :return:
    """
    conf = _get_yaml()

    if conf["pushbear_conf"]["is_pushbear"] and conf["pushbear_conf"]["send_key"].strip() != "":
        try:
            sendPushBearUrls = Pushbear
            data = {
                "sendkey": conf["pushbear_conf"]["send_key"].strip(),
                "text": "DW天气助手通知",
                "desp": msg
            }
            httpClint=WX_HTTPClient(0)
            sendPushBeaRsp = httpClint.send(sendPushBearUrls, data=data)
            if sendPushBeaRsp.get("code") is 0:
                _logger.info(u"已下发 pushbear 微信通知, 请查收")
            else:
                _logger.warn(sendPushBeaRsp)
        except Exception as e:
            _logger.error(u"pushbear 配置有误 {}".format(e))
    else:
        _logger.error(u"pushbear 配置有误,不能发送微信信息 ")
        pass


if __name__ == '__main__':
    sendPushBear(1)
