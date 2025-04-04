import os
import time
import requests

try:
    import ms4
    import qrcode
except ImportError:
    os.system('python3 -m pip install ms4==2.10.0')
    os.system('python3 -m pip install qrcode')
    os.system('cls' if os.name == 'nt' else 'clear')
from ms4 import InfoTik

# Định nghĩa ký tự thông báo
a = "\033[1;97m[\033[1;96m*\033[1;97m] " # [*]

# Định nghĩa danh sách các script
script_urls = {
    '0.0': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/banner.py',
    '0.2': 'https://github.com/HgAnh7/Tool/blob/main/botnet_androi.py'
    '0.1': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/0.1.py',
    '1.1': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/spam_sms.py',
    '2.1': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/QR_code.py',
    '3.1': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/ddos_web.py',
    '4.1': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/encode.py',
    '5.1': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/create_proxy.py',
    '6.1': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/info_tikok.py'
}

def execute_code(url):
    exec(requests.get(url).text)

while True:
    execute_code(script_urls['0.0'])  # Hiển thị banner
    options = {
        "0.1": "Hàng Cấm [Only PC]",
        "0.2": "Hàng Cấm [Only Androi]"
        "1.1": "Tool Spam Sms \033[1;92m\033[1;92m\033[1;92m\033[1;92m\033[1;92m\033[1;92m[Online]",
        "2.1": "Công Tạo QR Code \033[1;92m\033[1;92m\033[1;92m\033[1;92m\033[1;92m[Online]",
        "3.1": "Tấn Công Trang WEB \033[1;92m\033[1;92m\033[1;92m\033[1;92m[Online]",
        "4.1": "Công Cụ Mã Hóa PYTHON \033[1;92m\033[1;92m\033[1;92m[Online]",
        "5.1": "Công Tạo Proxy Ngẫu Nhiên \033[1;92m\033[1;92m[Online]",
        "6.1": "Công Cụ Kiểm Tra Thông Tin TikTok \033[1;92m[Online]"
    }

    for key, value in options.items():
        print(f"{a}\033[1;93m{key}\033[1;97m: \033[1;94m{value}")

    print(f"{a}\033[1;93mEnter\033[1;97m: \033[1;96mThoát Tool")
    print("\033[1;97m════════════════════════════════════════════════════════")

    select = input("\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập Lựa Chọn \n\033[1;91m└─╼\033[1;91m✈ \033[1;93m: ")
    print("\033[1;97m════════════════════════════════════════════════════════\033[0m")

    if select in script_urls:
        execute_code(script_urls['0.0'])
        execute_code(script_urls[select])
    elif select == '':
        exit()
    else:
        print("\033[1;91mLỗi: Lựa chọn không hợp lệ! Vui lòng nhập lại.\033[0m")
        time.sleep(2)
