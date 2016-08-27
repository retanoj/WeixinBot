#coding:utf-8

import random
import requests
import urllib

old_msg = {}
prefix = ""
GENERAL = ['呵呵', '去洗澡', '风太大, 你再说一遍?', '有能耐你再说一遍?']

def magic(cmd):
    if cmd == 'clean':
        global old_msg
        old_msg = {}
    elif cmd == '骂张冠男':
        return '张冠男你个臭傻逼'
    elif cmd.startswith('骂'):
        return random.choice(['啥?', '呵呵', '心平气和', '气~~急败坏'])
    else:
        url = 'http://www.xiaodoubi.com/simsimiapi.php?msg=' +urllib.quote_plus(cmd)
        try:
            return requests.post(url, data={'chat': cmd}, timeout=3).content
        except:
            return random.choice(GENERAL)


if __name__ == '__main__':
    print magic('骂a')