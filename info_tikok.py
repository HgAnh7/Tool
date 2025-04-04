# Share By @HgAnh_7

import os
import ms4
import time
from ms4 import InfoTik

while True:
    print('\033[1;97m╔═══════════════════════════════════╗')
    print('║ \033[1;96mCông Cụ Kiểm Tra Thông Tin TikTok \033[1;97m║')
    print('╚═══════════════════════════════════╝\033[0m')

    user = input('\033[1;97m[\033[1;96m*\033[1;97m] \033[1;97mNhập ID TikTok \033[1;97m(\033[1;33mBỏ "@"\033[1;97m): ').strip()
    info = InfoTik.TikTok_Info(user)

    if 'bad' in info['status']:
        print('⚠️\033[1;91mTên người dùng không hợp lệ!')
        time.sleep(3)
        for _ in range(5):  
            print('\033[A\033[K', end='')  # Di chuyển lên & xóa dòng
        continue
    elif 'ok' in info['status']:
        def get_info(key, default="⚠️ \033[1;91mKhông có dữ liệu!"):
            return str(info.get(key, default))

        name = get_info('name')
        followers = get_info('followers')
        following = get_info('following')
        like = get_info('like')
        video = get_info('video')
        flag = get_info('flag')
        country = get_info('country')
        Date = get_info('Date')
        ID = get_info('id')
        bio = get_info('bio')

    print(f'''\033[1;97m╔════════════════════════════════════\033[0m
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mTên người dùng: \033[1;97m@{user}             
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mTên hiển thị: \033[1;97m{name}           
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mNgười theo dõi: \033[1;97m{followers}         
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mĐang theo dõi: \033[1;97m{following}         
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mLượt thích: \033[1;97m{like}       
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mSố video: \033[1;97m{video}      
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mCờ: \033[1;97m{flag}            
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mQuốc gia: \033[1;97m{country}        
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mNgày tạo: \033[1;97m{Date}        
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mID: \033[1;97m{ID}           
\033[1;97m[\033[1;96m*\033[1;97m] \033[1;96mTiểu sử: \033[1;97m{bio} 
\033[1;97m╚════════════════════════════════════\033[0m''')
    print('\033[1;97m[\033[1;96m*\033[1;97m] Enter Để Thoát Tool')
    print('\033[1;97m[\033[1;96m*\033[1;97m] Nhập Kí Tự Bất Kì Để Tiếp Tục...')

    select = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập Lựa Chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;93m: ').strip()
    if select == '':
        print("\033[1;91mĐang Thoát Tool.\033[0m")
        time.sleep(1.5)
        break
    else:
        for _ in range(21):  
            print('\033[A\033[K', end='')  # Di chuyển lên & xóa dòng
