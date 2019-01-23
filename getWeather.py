# -*- coding: utf8 -*-
import json
import random
import requests
from time import sleep
import logging
import logging.config
import logging.handlers
import myUrllib
import  Config.conf
from Config.conf import _get_yaml
weather_data = {}
_logger = logging.getLogger("daily")

class Weather(object):
    def __init__(self, city_name):
        self.city_name = city_name
        weather_data['city_name'] = city_name
        _logger.info("正在获取{}天气信息\n".format(city_name))
        # 天气预报URL
        self.forecast_url ='https://free-api.heweather.com/s6/weather/forecast?parameters'
        # 生活指数
        self.lifestyle_url = 'https://free-api.heweather.com/s6/weather/lifestyle?parameters'
        self.parametres = {
            'location': self.city_name,
            'key':  'f4b3c9e903d047c09b0ea5923c62a21e',  # 注册和风天气会给你一个KEY
            'lang': 'zh',
            'unit': 'm'
        }

        self.weatherInfo = dict()
        self.message = []

    def __str__(self):
        return " ".join(self.message)

    def getMessage(self):
        return self.message

    def getWeatherInfo(self):
        for i in range(1):
            self.weatherUrl = "http://www.sojson.com/open/api/weather/json.shtml?city={}".format(self.city_name)
            result = json.loads(myUrllib.get(self.weatherUrl))
            if "status" in result and result["status"] is 200 and result["data"]:
                self.weatherInfo = result["data"]["forecast"][0]   # 获取今日天气预报
                break
            else:
                print(result["status"])
            sleep(1)

    def get_heweatherInfo(self):
       new_data = []
       try:
            response = requests.get(self.forecast_url, params=self.parametres)
            #r = json.loads(json.dumps(response.text, ensure_ascii=False, indent=1))
            r = json.loads(response.text)
            weather_forecast = r['HeWeather6'][0]['daily_forecast']
            data = weather_forecast[0]
            for data in weather_forecast:
                new_obj = {}
                # 日期
                new_obj['date'] = data['date']
                # 日出时间
                new_obj['sr'] = data['sr']
                # 日落时间
                new_obj['ss'] = data['ss']
                # 月升时间
                new_obj['mr'] = data['mr']
                # 月落时间
                new_obj['ms'] = data['ms']
                # 最高温度
                new_obj['tmp_max'] = data['tmp_max']
                # 最低温度
                new_obj['tmp_min'] = data['tmp_min']
                # 白天天气状况描述
                new_obj['cond_txt_d'] = data['cond_txt_d']
                # 晚间天气状况描述
                new_obj['cond_txt_n'] = data['cond_txt_n']
                # 风向
                new_obj['wind_dir'] = data['wind_dir']
                # 风力
                new_obj['wind_sc'] = data['wind_sc']
                # 降水概率
                new_obj['pop'] = data['pop']
                # 降水量
                new_obj['pcpn'] = data['pcpn']
                # 紫外线强度指数
                new_obj['uv_index'] = data['uv_index']
                # 能见度
                new_obj['vis'] = data['vis']
                new_data.append(new_obj)
            weather_data['weather'] = new_data
       except Exception as e:
           _logger.exception(e)

    def get_heweatherLifeStyleInfo(self):
        try:
            response = requests.get(self.lifestyle_url, params=self.parametres)
            # r = json.loads(json.dumps(response.text, ensure_ascii=False, indent=1))
            r = json.loads(response.text)
            lifestyle = r['HeWeather6'][0]['lifestyle']
            weather_data['lifestyle'] = lifestyle
            # 生活指数类型 -drsg 穿衣建议
            #weather_data['drsg'] = lifestyle[1]['txt']
        except Exception as e:
            _logger.exception(e)

    def main(self):
        # self.getWeatherInfo()
        self.get_heweatherInfo()
        self.get_heweatherLifeStyleInfo()
        return weather_data

if __name__ == '__main__':
    _logger.info("正在请求%s的天气" % str("北京"))
    w = Weather("北京")
    print (w.main())
    _logger.debug("已经成功请求%s的天气"%str("北京") )


