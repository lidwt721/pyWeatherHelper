#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The Entry """

import logging
import logging.config
import logging.handlers
import getWeather
import encodeMessage
import  Config.conf as conf
from Config.conf import _get_yaml
from Config.UnicodeFilter import Code
from Config.pushbearConf import sendPushBear
__author__ = 'lidwt'

def main_program():
    Code()    
    logging.config.dictConfig(conf.log_setting)
    log = logging.getLogger("daily")
    log.info(u"main程序开始运行!")
    try:
        weather_conf = _get_yaml()["Weather"]
        city_num = len(weather_conf["city_name"])
        for data in weather_conf["city_name"]:
            city_name = data
            w = getWeather.Weather(city_name).main()
            # print(w['weather'][0]['date'])
            # print(w['lifestyle'][1]['txt'])
            # log.info("获取天气信息成功!")
            m = encodeMessage.Message(w)
            m.main()
            msg=m.getMessage()
            info = ""
            # print(info)
            for data in msg:
                # print(data)
                info+=data
                info += "\n"
            # print(info)
            sendPushBear(info)
            # log.info(m.getMessage())
    except Exception,e:
        log.info(u"程序运行出错!")
        log.error(e)
    finally:
        log.info(u"程序停止运行!")

if __name__ == '__main__':
    main_program()