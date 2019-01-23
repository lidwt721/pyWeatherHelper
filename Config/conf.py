# -*- coding: utf8 -*-

import platform
import os
import sys
import yaml
import DevParams

import logging
import logging.config
import logging.handlers

app_path = os.path.abspath(os.path.dirname(sys.argv[0]))
# log setting
log_setting = {
    'version': 1,
    'formatters': {
        'std': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'run_log_handler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'std',
            'filename': app_path + '/_runtime/Log/run_log.log',
            'when': 'midnight',
            'backupCount': 30
        },
        'error_log_handler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'std',
            'filename': app_path + '/_runtime/Log/error_log.log',
            'when': 'midnight',
            'backupCount': 30
        },
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std'
        }
    },
    'loggers': {
        'daily': {
            'handlers': ['run_log_handler', 'console_handler'] if DevParams.debug else ['run_log_handler','error_log_handler'],
            'level': 'DEBUG',
        },
        'tagError':{
            'handlers': ['run_log_handler', 'error_log_handler', 'console_handler'] if DevParams.debug else ['run_log_handler', 'error_log_handler'],
        }
    }
}
def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(__file__) + '/conf.yaml')
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s.decode() if isinstance(s, bytes) else s


if __name__ == '__main__':
    print(app_path)
    print(_get_yaml())
    _logger = logging.getLogger("daily")
    _logger.warn(app_path)
