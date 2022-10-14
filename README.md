# 提醒喝水小助手
基于微信测试公众号的提醒功能
此功能仅用于个人娱乐用途,暂不具备用户自订阅模板信息,批量获取用户信息

## 部署
- redis
- Linux : Crontab

## 配置
- 申请微信测试接口:
	- https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

- 添加模板

- 配置config.yaml文件:
	- 填写apiid
	- 填写apisecret
	- 填写模板id
	- ...


## 原理
- cron设置每小时提醒,这个时候会查询redis数据库看今日日期有没有变化,
	- 没有变化: 继续发送今天的任务,提醒到指定次数会更新 `start` 为0
	- 有变化:
		- 更新`start` 参数为 1

