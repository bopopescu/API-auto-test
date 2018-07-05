#coding=utf8

import json
import traceback
import requests


url = "http://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET"


try:
    #Post接口调用
    response = requests.request("GET", url, headers=headers, params=querystring)

    #对http返回值进行判断，对于200做基本校验
    if response.status_code == 40013:
        results = json.loads(response.text)
        if results['total'] == 191:
            print "Success req"
        else:
            print "Fail"
            print results['total']
    else:
        #对于http返回非200的code，输出相应的code
        raise Exception("http error info:%s" %response.status_code)
except:
    traceback.print_exc()