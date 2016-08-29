# coding:utf-8

import random
import requests
import js2py

old_msg = {} #old_msg[id] = {'type':xx, 'content':xx}
prefix = "--"
CMD_DONE = 'command done'
fake_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0'}


def magic(cmd):
    if cmd == 'clean':
        global old_msg
        old_msg = {}
    elif cmd == '骂张冠男':
        return '张冠男你个臭傻逼'
    elif cmd.startswith('骂'):
        return random.choice(['啥?', '呵呵', '要心平气和', '你气~~急败坏'])
    elif cmd == '天气':
        try:
            f_headers = fake_headers
            f_headers['Referer'] = 'http://www.weather.com.cn'
            j = requests.get('http://d1.weather.com.cn/dingzhi/101010100.html', headers=f_headers, timeout=5)
            j.encoding = 'utf-8'
            j = js2py.eval_js(j.text.split(';')[0])['weatherinfo']
            return "%s | %s | %s  ~ %s" % (j['cityname'], j['weather'], j['tempn'], j['temp'])
        except Exception ,e:
            pass
    return CMD_DONE

if __name__ == '__main__':
    print magic('天气')