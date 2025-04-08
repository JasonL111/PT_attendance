# PT_attendance

这是一个用于自动签到并通过 Telegram 发送签到结果的 Python 脚本

## 语言 Language
[English](https://github.com/JasonL111/PT_attendance/blob/main/README.en_US.md)

## 运行环境

- Python 3.x
- 需要安装以下 Python 库：
  - `requests`
  - `python-dotenv`

## 安装步骤

1. 克隆或下载本仓库
```bash
git clone https://github.com/JasonL111/PT_attendance.git
```
2. 安装所需依赖库：

```bash
pip install requests python-dotenv
```
3. 在`PT_attendance`目录下创建一个 .env 文件，填入以下信息：
```bash
# Telegram Bot 相关信息
TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id

# Cookie 信息
c_secure_uid=your_uid_cookie
c_secure_pass=your_pass_cookie
c_secure_ssl=your_ssl_cookie
c_secure_tracker_ssl=your_tracker_ssl_cookie
c_secure_login=your_login_cookie
attendance_url=your_attendance_url
domain=your_pt_website_domain
```
- TOKEN: 你的 Telegram 机器人 Token，创建 Telegram 机器人时获得。

- CHAT_ID: 你要接收通知的 Telegram 用户聊天 ID。

- c_secure_*: 用于签到的 cookies。你可以通过浏览器的开发者工具获取这些 cookies。

- attendance_url:你的签到界面的URL

- domain:一般是网站首页的URL

## 使用说明
直接运行脚本即可进行签到：

```bash
python main.py
```
