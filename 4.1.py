# Share By @HgAnh_7

import os
import sys
import re
import time
import random
import requests

class free_proxy:
	def __init__(self):
		url = 'https://free-proxy-list.net/'
		proxies = []
		print('\033[1;97m╔═══════════════════════════╗')
		print('║ \033[1;96mCông Tạo Proxy Ngẫu Nhiên \033[1;97m║')
		print('╚═══════════════════════════╝\033[0m')
		proxy1 = requests.get(url).text
		proxy2 = re.findall(r'<tr><td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+?)</td>', proxy1)
		for x in proxy2:
			proxies.append(':'.join(x))
		while True:
		    try:
		        tanya_total = int(input('\033[1;97m[\033[1;96m*\033[1;97m] Nhập Số Lượng Cần Tạo: '))
		        break  # Thoát vòng lặp nếu nhập đúng số nguyên
		    except ValueError:
		        print("\033[1;91mLỗi: Vui lòng nhập một số nguyên hợp lệ!")
		        time.sleep(3)
		        for _ in range(2):
		        	print('\033[A\033[K', end='')
		
		print('     ⏳ \033[1;96mĐang Xử Lý...')
		time.sleep(3)
		print('\033[A\033[K', end='')
		for total in range(tanya_total):
			total +=1
			proxy = random.choice(proxies)
			print('    proxy %s -> %s'%(total, proxy))
		ask = input('\033[1;97m[\033[1;96m*\033[1;97m] Bạn Có Muốn Tạo Thêm Không? \033[1;92m(y/n)\033[97m:\033[0m ')
		if ask in ['Y', 'y', '']:
			for _ in range(tanya_total + 6):
				print('\033[A\033[K', end='')  # Di chuyển lên & xóa dòng
			free_proxy()
		elif ask in ['n', 'N']:
			exit()
try:
	free_proxy()
except Exception as e:
	exit(str(e))
