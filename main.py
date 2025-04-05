import requests
from dotenv import load_dotenv
import os

load_dotenv()

def success():
    TOKEN=os.getenv('TOKEN')
    CHAT_ID=os.getenv('CHAT_ID')
    TEXT = "🤖 签到成功"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": TEXT
    }
    res = requests.post(url, data=payload)
def failed():
    TOKEN=os.getenv('TOKEN')
    CHAT_ID=os.getenv('CHAT_ID')
    TEXT = "🤖 签到失败"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": TEXT
    }
    res = requests.post(url, data=payload)   

def send_request():
    session = requests.Session()

    c_secure_uid = os.getenv('c_secure_uid')
    c_secure_pass = os.getenv('c_secure_pass')
    c_secure_ssl = os.getenv('c_secure_ssl')
    c_secure_tracker_ssl = os.getenv('c_secure_tracker_ssl')
    c_secure_login = os.getenv('c_secure_login')
    request_domain=os.getenv('domain')
    
    # 使用session.cookies.set方法设置每个cookie，指定domain和path
    session.cookies.set('c_secure_uid', c_secure_uid, domain=request_domain, path='/')
    session.cookies.set('c_secure_pass', c_secure_pass, domain=request_domain, path='/')
    session.cookies.set('c_secure_ssl', c_secure_ssl, domain=request_domain, path='/')
    session.cookies.set('c_secure_tracker_ssl', c_secure_tracker_ssl, domain=request_domain, path='/')
    session.cookies.set('c_secure_login', c_secure_login, domain=request_domain, path='/')

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        # Referer栏为可选，可根据需求填写
        #"Referer": "your-url",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
        "TE": "trailers"
    }
    
    # 发送请求
    attendance_url=os.getenv('attendance_url')
    response = session.get(
        attendance_url,
        headers=headers
    )
    check(response)
def check(response):
    print(response.text)
    if("已连续签到" in response.text):
        success()
    else:
        failed()
def main():
   send_request()
if __name__=="__main__":
    main()