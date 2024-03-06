from wxauto import WeChat
import time
import yaml
import requests
from optML import mxSendToML

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
        resMsg = mxSendToML(msg)
        # 回复收到
        chat.SendMsg(resMsg)  # 回复收到
    time.sleep(wait)

print('wxauto测试完成！')