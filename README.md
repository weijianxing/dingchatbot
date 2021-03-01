# dingchatbot
测试自动化脚本 钉钉消息推送 通用sdk 钉钉消息接口封装

常见用法：

WEBHOOK_TOKEN = "https://oapi.dingtalk.com/robot/send?access_token=xxxxxx"
    ding = DingtalkChatbot(webhook=WEBHOOK_TOKEN)
    title = "iOS测试ding python sdk"
    at_mobiles= ["1352030xxxx","魏建星"]
    # at_mobiles = ["1352030xxxx"]
    ding.send_monitorMsg(title=title,subTitle="xxxx场景用例执行" ,owner="骆老师",  at_mobiles=at_mobiles )
    ding.send_failInfo(title=title,subTitle="xxxx场景用例执行" ,owner="骆老师",  at_mobiles=at_mobiles , caseInfo="xxx 测试case " )
