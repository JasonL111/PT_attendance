import requests
import os

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
    
    # 使用session.cookies.set方法设置每个cookie，指定domain和path
    session.cookies.set('c_secure_uid', c_secure_uid, domain='pt.soulvoice.club', path='/')
    session.cookies.set('c_secure_pass', c_secure_pass, domain='pt.soulvoice.club', path='/')
    session.cookies.set('c_secure_ssl', c_secure_ssl, domain='pt.soulvoice.club', path='/')
    session.cookies.set('c_secure_tracker_ssl', c_secure_tracker_ssl, domain='pt.soulvoice.club', path='/')
    session.cookies.set('c_secure_login', c_secure_login, domain='pt.soulvoice.club', path='/')

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://pt.soulvoice.club/index.php",
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
    response = session.get(
        "https://pt.soulvoice.club/attendance.php",
        headers=headers
    )
    check(response)
def check(response):
    print(response.text)
    if(response.status_code!=200):
        if("未登录" in response.text):
            failed()
    else:
        success()
def main():
   send_request()
if __name__=="__main__":
    main()