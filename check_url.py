import os
import re
import requests
from tqdm import tqdm
from time import sleep

file_name = input("Nhập tên file chứa URL (ví dụ: urls.txt): ").strip()

# Kiểm tra file tồn tại
if not os.path.exists(file_name):
    print(f"❌ Không tìm thấy file: {file_name}")
    exit()

# Đọc toàn bộ nội dung file
with open(file_name, 'r', encoding='utf-8') as f:
    content = f.read()

# Tìm tất cả URL hợp lệ bằng regex
urls = list(set(re.findall(r'https?://[^\s]+', content)))  # loại bỏ trùng

working_urls = []
broken_urls = []

headers = {'User-Agent': 'Mozilla/5.0'}

# Kiểm tra từng URL
for url in tqdm(urls, desc="🔎 Đang kiểm tra URL", unit="url"):
    for attempt in range(3):  # thử 3 lần nếu lỗi
        try:
            response = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
            if response.status_code in [200, 301, 302, 403, 405]:
                working_urls.append(url)
            else:
                broken_urls.append(url)
            break  # nếu thành công, thoát vòng lặp thử
        except Exception as e:
            if attempt == 2:
                print(f"⚠️ Lỗi với {url}: {e}")
                broken_urls.append(url)
            else:
                sleep(1)  # đợi 1 giây rồi thử lại

# Ghi kết quả ra file
with open('working_urls.txt', 'w', encoding='utf-8') as f:
    f.writelines(url + '\n' for url in working_urls)

with open('broken_urls.txt', 'w', encoding='utf-8') as f:
    f.writelines(url + '\n' for url in broken_urls)

# Thống kê
print("\n==== KẾT QUẢ ====")
print(f"Tổng URL tìm thấy: {len(urls)}")
print(f"✅ Hợp lệ: {len(working_urls)}")
print(f"❌ Bị lỗi: {len(broken_urls)}")
print("Kết quả đã được lưu vào 'working_urls.txt' và 'broken_urls.txt'")
