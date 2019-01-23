# -*- coding: utf8 -*-
import json
import random
import requests
from time import sleep
import myUrllib
import logging
import logging.config
import logging.handlers
_logger = logging.getLogger("daily")

class Message(object):
    def __init__(self, weatherInfo):
        self.weatherInfo = weatherInfo
        self.message = []
        # 每日一句URL 金山词霸开放平台-api   获取地址：http://open.iciba.com/?c=api
        self.iciba_ds_url = 'http://open.iciba.com/dsapi/'

    def __str__(self):
        return " ".join(self.message)

    def getMessage(self):
        return self.message

    def sendTemplate(self):
        template = [
            "新的一天又来啦，给小主念早安早安早安，重要的事情说三遍，\n",
            "早安哦，催小主快带你起床啦，\n",
            "坚持不懈的小主奉上早安，我是不会忘记的，\n",
            "早晨，是一个美妙的开端，小主早安哦，\n",
            "小主，我有一千种给你说早安的方式，今天第一千种,\n",
            "每天都是改变命运的机会，小主，早安呐，\n",
            "早安，太阳，早安，地球，早安，中国，早安，亲爱的小主，快起来了，\n",
            "我想告诉全世界的人，你是最漂亮的，早安！小主，\n",
            "太阳冉冉升起，清风柔柔吹起,早安，\n",
            "让爱你的人放心，让恨你的人失落, 一碗鸡汤请小主喝，早安，\n",
            "我想你一定很忙，所以只看前三个字就好啦，早安呀！\n",
            "想不出来今天说啥了，嗯，早安，\n",
            "掀被而起，君临天下,haha,\n",
            "帅的人已醒 丑的人还在沉睡,丑的是指的我，早安，\n",
            "good   morning。。。。。\n",
            "晚安，哦，说错了，是早安，小主，\n"
        ]
        self.message.append(template[random.randint(0, len(template))])

    def sendMessageByTemperature(self):
        self.message.append("当前时间:{}\n".format(self.weatherInfo['weather'][0]['date']))
        self.message.append("城市:{}\n".format(self.weatherInfo['city_name']))
        self.message.append("白天天气:{0} {1} \n".format(self.weatherInfo['weather'][0]['cond_txt_d'],self.weatherInfo['weather'][0]['wind_dir']))
        self.message.append("夜间天气:{}\n".format(self.weatherInfo['weather'][0]['cond_txt_n']))
        self.message.append("今天{0}: 气温: {1}°/{2}°\n".format(self.weatherInfo['weather'][0]['date'],self.weatherInfo['weather'][0]['tmp_min'],self.weatherInfo['weather'][0]['tmp_max']))
        self.message.append("未来{0}: 气温: {1}°/{2}°\n".format(self.weatherInfo['weather'][1]['date'],
                                                           self.weatherInfo['weather'][1]['tmp_min'],
                                                           self.weatherInfo['weather'][1]['tmp_max']))
        self.message.append("未来{0}: 气温: {1}°/{2}°\n".format(self.weatherInfo['weather'][2]['date'],
                                                           self.weatherInfo['weather'][2]['tmp_min'],
                                                           self.weatherInfo['weather'][2]['tmp_max']))
        self.message.append("穿衣建议: {}\n".format(self.weatherInfo['lifestyle'][1]['txt']))



    def sendMessageByWantTosay(self):
        pass

    def get_dsInfo(self):
        try:
            response = requests.get(self.iciba_ds_url)
            # r = json.loads(json.dumps(response.text, ensure_ascii=False, indent=1))
            r = json.loads(response.text)
            content = r['content']
            print(content)
            note = r['note']
            print(note)

        except Exception as e:
            _logger.exception(e)

    def main(self):
        self.sendMessageByTemperature()
        self.get_dsInfo()
        self.sendTemplate()
        return "".join(self.message)

if __name__ == '__main__':
    w = Message("北京")
    print(w.main())
