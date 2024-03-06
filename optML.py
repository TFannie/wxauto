import time
import yaml
import requests
import base64
from Crypto.Cipher import AES
import hashlib
import wxauto.utils as utils
from json import loads

  # 返回bytes

# 1、读取监听群消息
def mxSendToML(data):
    with open('./initData.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    url = result['user']['url']
    timestamp=int(time.time()*1000)
    appSecret_hash=hashlib.sha256(str.encode(result['user']['appSecret'])).hexdigest()
    digna= f"{result['user']['appId']}:{hashlib.sha256(str.encode(appSecret_hash)).hexdigest()}{timestamp}"
    header = {'ContentType': 'application/json'
        , 'X-Signa': base64.b64encode(bytes(digna,'utf-8')).decode("utf-8")
        , 'X-Appid': result['user']['appId']
        , 'X-Timestamp': str(timestamp)}
    assy=AES.new(bytes(str.encode(result['user']['appSecret'])),AES.MODE_ECB)
    str1=str(result['user']['userId'])
    assyr=assy.encrypt(utils.add_to_16(str1))
    data = {'chatbotId': result['user']['chatbots'][0],
            'content': '你好',
            'userId': base64.b64encode(assyr),
            'secretLen': 32,
            'platform': '交付机器人'}

    response = requests.post(url, headers=header, data=data)
    # 回复收到
    print(response)
    return loads(response.text)['data']['result']