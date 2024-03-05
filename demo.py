from wxauto import WeChat
import time
import yaml
import requests

# 1、读取监听群消息
with open('./initData.yaml', 'r', encoding='utf-8') as f:
    result = yaml.load(f.read(), Loader=yaml.FullLoader)

wx = WeChat()


# 2、遍历监听目标
for i in result['listen']:
    wx.AddListenChat(who=i)  # 添加监听对象并且自动保存新消息图片
print('监听添加成功！')
# 持续监听消息，并且收到消息后回复“收到”
wait = 6  # 设置10秒查看一次是否有新消息

# 3、配置请求信息
url = 'http://117.136.240.114/gtw-ai-test/cmic-ai-platform-test'
header = {'ContentType': 'application/json'
    , 'X-Signa': xsigna
    , 'X-Appid': result['user']['appId']
    , 'X-Timestamp': time.time()}

data = {'chatbotId': result['user']['chatbots'][0],
        'content': 'content',
        'userId': result['user']['userId'],
        'secretLen': 11,
        'platform': '111',
        'platformAccount': '111'}
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        msg = msgs.get(chat)   # 获取消息内容
        # ===================================================
        # 处理消息逻辑
        #
        # 处理消息内容的逻辑每个人都不同，按自己想法写就好了，这里不写了
        #
        # ===================================================
        # 3、消息列表分开处理
        # 4、消息响应
        # 发送 POST 请求
        response = requests.post(url, headers=header,data=data)
        # 回复收到
        chat.SendMsg(response.text)  # 回复收到
    time.sleep(wait)

print('wxauto测试完成！')