#coding:utf-8

import json
import urllib.request
import random

tuling='26af02f18c8a444d916de0ff23ad1ff2'
api_url = "http://openapi.tuling123.com/openapi/api/v2"

def get_message(message,userid):
    req = {
    "perception":
    {
        "inputText":
        {
            "text": message
        },

        "selfInfo":
        {
            "location":
            {
                "city": "深圳",
                "province": "广州",
                "street": "1856号街道"
            }
        }
    },
    "userInfo": 
    {
        "apiKey": tuling,
        "userId": userid
    }
    }
    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)
    results_text = response_dic['results'][0]['values']['text']
    return results_text

if __name__ == "__main__":
    response_str = get_message("我爱音乐", random.randint(1,1000))
    print(response_str)
