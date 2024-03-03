from wxauto import WeChat
import time

wx = WeChat()

# 发送消息
#who = 'TFannie'
#for i in range(3):
#    wx.SendMsg(f'wxauto测试{i+1}', who)

# 获取当前聊天页面（文件传输助手）消息，并自动保存聊天图片
# msgs = wx.GetAllMessage(savepic=True)
# for msg in msgs:
#    print(f"{msg[0]}: {msg[1]}")

# 指定监听目标
listen_list = [
    'TFannie',
    '文件传输助手'
]
for i in listen_list:
    wx.AddListenChat(who=i)  # 添加监听对象并且自动保存新消息图片
print('监听添加成功！')
# 持续监听消息，并且收到消息后回复“收到”
wait = 10  # 设置10秒查看一次是否有新消息
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

        # 回复收到
        chat.SendMsg('收到')  # 回复收到
    time.sleep(wait)

print('wxauto测试完成！')