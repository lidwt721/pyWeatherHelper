# -*- coding: utf8 -*-
from Config.pushbearConf import sendPushBear

import unittest

def testPushbear(self):
    """
    实测pushbear是否可用
    :return:
    """
    sendPushBear("pushbear 微信通知测试一下")

if __name__ == '__main__':
    unittest.main()