# PT_attendance
This is a Python script for automatic attendance check-in and sending check-in results via Telegram

## 语言 Language
[中文](https://github.com/JasonL111/PT_attendance)

## Environment
- Python 3.x
- Required Python libraries:
 - `requests`
 - `python-dotenv`

## Installation Steps
1. Clone or download this repository
```bash
git clone https://github.com/JasonL111/PT_attendance.git
```
2. Install required dependencies:
```bash
pip install requests python-dotenv
```
3. Create a .env file with the following information in the `PT_attendance` directory:
```bash
# Telegram Bot Information
TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
# Cookie Information
c_secure_uid=your_uid_cookie
c_secure_pass=your_pass_cookie
c_secure_ssl=your_ssl_cookie
c_secure_tracker_ssl=your_tracker_ssl_cookie
c_secure_login=your_login_cookie
attendance_url=your_attendance_url
domain=your_pt_website_domain
```
- TOKEN: Your Telegram bot token, obtained when creating a Telegram bot.
- CHAT_ID: The Telegram user chat ID where you want to receive notifications.
- c_secure_*: Cookies used for check-in. You can obtain these cookies through your browser's developer tools.
- attendance_url: The URL of your check-in page
- domain: Generally the URL of the website homepage

## Usage Instructions
Simply run the script to perform the check-in:
```bash
python main.py
```