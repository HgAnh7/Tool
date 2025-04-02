import os
import time
import qrcode
from PIL import Image

print('\033[1;97m╔══════════════════╗')
print('║ \033[1;96mCông Tạo QR Code \033[1;97m║')
print('╚══════════════════╝\033[0m')

def generate_qr_terminal(data):
    # Tạo QR code
    qr = qrcode.QRCode(
        version=1,  # Kích thước QR code (1 là nhỏ nhất)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Mức độ chịu lỗi
        box_size=20,  # Kích thước ô vuông(giá trị ban đầu =2)
        border=1,  # Viền xung quanh QR
    )
    qr.add_data(data)
    qr.make(fit=True)

    # In QR code dưới dạng ASCII
    qr.print_ascii()

    # Hỏi người dùng có muốn lưu QR code dưới dạng ảnh không
    save_image = input("Bạn có muốn lưu QR code dưới dạng ảnh không? (y/n): ").lower()
    if save_image == 'y':
        file_name = input("Lưu QR code (định dạng '.PNG') với tên: ") + '.png'  # Thay .jpg bằng .png
        # Tạo ảnh QR code
        img = qr.make_image(fill_color="#d777f7", back_color="white")
        img.save(file_name, "PNG")  # Lưu ảnh dưới dạng PNG
        for _ in range(15):
            print("\033[A\033[K", end="")
        print(f"QR code đã được lưu với tên: {file_name}")
    else:
        print("...")
        time.sleep(1.5)

if __name__ == "__main__":
    while True:
        text = input("Nhập nội dung QR code (gõ 'Enter' để thoát): ")
        if text.lower() == "":  # Dừng chương trình khi nhấn Enter
            print("\033[A\033[K", end="")
            for i in range(3, 0, -1):  # Đếm ngược từ 3 đến 1
                print(f"\033[1;91mThoát chương trình trong:\033[1;97m {i}", end="\r")
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            break  # Dừng vòng lặp nếu 'Enter'
        generate_qr_terminal(text)
