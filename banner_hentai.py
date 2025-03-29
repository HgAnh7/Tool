import os
import random

# Danh sách các banner ASCII
banners = [
    """
⠀⠀⠀⠀⠀⣸⢸⢸⢸⡏⠂⠀⣾⠥⡇⠥⡄⣹⠀⠀⢸⣿⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⢸⢸⠔⡇⣾⡄⣿⢀⠀⠀⠑⢾⠀⢀⢸⡿⢡⢁⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠈⡼⣇⠇⡿⠯⡟⠂⢴⣶⣶⡷⡄⠸⣸⡇⡏⡾⠀⠀⠀⠀
⠀⠀⠀⠀⢸⢵⢣⢳⣞⣶⣿⢠⡏⠂⠘⠛⢉⢱⠀⣧⡏⡇⡗⣷⡆⠀⠀⠀
⠀⠀⠀⠀⡈⣸⢣⢆⣫⠛⠋⠀⠀⠀⠀⠀⢸⡆⣼⢁⣇⡇⡇⡁⡇⠀⠀⠀
⠀⠀⠀⠀⡇⡏⡎⣌⣎⡳⠄⠀⠀⠀⠀⠠⢻⣶⣿⣾⢸⢰⡁⡇⡟⠀⠀⠀
⠀⠀⠀⠀⠇⣧⣿⣿⣼⣿⣦⣄⡀⠀⢀⢔⠟⣿⣻⡇⢸⡾⣇⠁⡇⠀⠀⠀
⠀⠀⠀⠀⢀⢸⣿⢹⣿⣿⣿⣿⠈⠉⠀⠁⠀⢷⡟⠃⣾⢳⡟⠀⡇⠀⠀⠀
⠀⠀⠀⠀⢘⠸⠿⠻⠿⠛⠋⠁⠀⠁⠀⠁⠔⢀⠉⠓⠛⠛⠧⣰⠇⠀⠀⠀
⠀⠀⢠⠊⠀⠀⠀⠀⠀⠀⠀⠉⠁⠢⠤⠊⠁⠀⠀⠀⠀⠀⠀⠈⠉⢆⠀⠀
⠀⠀⠈⠀⢀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⢸⠀⠀
⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⣸⠀⠀
⠀⡐⠁⡠⠔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀
⢰⠀⡌⢤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠈⠄
⢸⠀⠃⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠸⡀⠘
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⠀⢆⠀⠀⠀⠀⠀⠀⠀⠁⠁⢸⠃⢰
⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⡠⢼⠋⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠒⠁⢠⠂
⠀⠀⠋⠑⢶⢠⠤⠀⢒⠨⠒⠁⠀⠀⠀⠀⠐⢕⠤⣀⠀⠀⠀⠀⣀⢴⠁⠀
⠀⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢹⠩⠋⠀⠈⡄⠀
    """,
    """
⠉⠉⠉⠉⠉⠉⠉⠉⠉⣉⠯⡽⣿⣧⣼⣯⣙⡏⠉⠉⠫⡷⠶⡴⠦⢶⠶⠆⠤⠀
⣤⣤⣤⣤⣤⣤⣤⡴⠋⣑⢞⠍⠀⣸⣆⠀⠀⠗⣶⠀⠀⠰⠀⠈⠁⠁⠀⠉⠀⠀
⠿⠿⠿⠿⠿⢻⡿⣽⣿⡿⢳⡖⣨⠏⠸⡜⡀⢡⠈⡆⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠁⡻⢿⢣⣟⣛⠉⢡⠃⠇⡇⠀⠀⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣤⣤⣤⣤⣤⣼⠀⣇⠄⣆⠉⠉⠉⠘⣜⣼⢇⠜⢀⣿⣤⠤⠤⠄⠀⠀⠀⠀⠀⠀
⣿⣿⢇⡐⠃⠙⣷⣻⠑⡄⠀⠀⠀⠀⠀⠑⢪⣪⡾⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠁⠐⠁⠀⠀⠘⢿⣧⡏⠢⣀⠀⠀⣀⡰⠟⠁⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡃⠀⠀⠀⡠⠊⠉⠉⠙⠥⠀⣀⢙⣯⡥⠤⠤⠤⣀⣇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠃⠀⠀⠀⡤⠀⠀⠉⠉⠐⠢⠀⠐⠂⠒⠳⢌⣀⠀⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠈⡄⠀⠀⢰⠀⠀⠀⠀⠓⠀⠀⠈⠆⠀⠀⠀⠀⠽⣴⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⣀⣵⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡆⠀⠀⢱⠤⠀⠀⠀⠤⠐⠊⠈⠢⣀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣧⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⡗⠊⠹⠀⠀⠀⠀⠀⠀⢻⠟
⠀⠀⠀⣿⣿⣿⡆⠀⠀⣷⡠⠀⠀⠀⠀⠀⠀⠘⠀⠳⡀⠀⠀⡆⠀⠀⠀⠀⢸⠀
⠀⠀⠀⣽⣿⣿⡗⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡆⡇⠀⠀⠀⠀⠈⠀
⠀⠀⠀⣾⠿⣱⣷⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠇⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠓⠛⠛⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢀⠆⠀⠀⠑⣸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠈⠠⡀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠹⠀⠀⢋
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠸
⠀⢀⠀⠀⢀⡀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠢⠁⢠⣿⡇⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    """
 ⠀⠀⠀⠀⠀⠀⠈⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠉⢠⠃⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡀⢃⢸⠀⠀⠀
⠀⠀⠀⣀⣤⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⣼⣿⠿⠧
⠀⢠⣾⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⣿⠏⠀⢀
⠹⣿⣿⣿⡏⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢆⠀⠀⣸⠃⢀⡔⠁
⠀⠘⢿⣿⣧⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⠏⠀⢀⣿⡶⡡⢀⠀
⢠⠐⡀⢻⣿⣦⡀⠀⠀⠀⣀⠀⠀⠀⠀⠰⡄⠀⠀⠀⠀⠀⠀⢀⢼⣿⠡⠁⡎⠀
⡀⠇⢱⡀⣿⣿⣿⣦⣤⣀⡤⠞⠀⠀⠀⠀⠙⢦⣀⣀⠀⣀⡤⠋⣾⣿⣅⢼⠁⠨
⡇⠘⢠⢇⢹⣿⣿⣿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠉⠁⠀⢸⣿⣿⣷⡘⠀⠀
⢃⢀⠌⠀⠼⢻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢿⣿⣿⣿⠛⠚⠀
    """,
    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⡀⠀⠀⢀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡏⢠⣧⡀⣿⣷⡆⢯⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢧⢿⣿⡿⠟⠻⢻⢹⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⢘⣧⢣⡀⠀⠀⣸⣴⡏⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣽⣼⢿⣆⣋⠕⢉⡜⡈⠧⠉⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠹⠩⡿⠉⡏⡆⠚⠇⣆⠂⡄⢀⠇⠀⠀⠀⣠⠖⠈⠑⢆
⠀⠀⠀⠀⠀⠀⠈⡄⢡⡁⣳⡿⠁⠀⠈⠛⠀⠛⠎⡆⢀⡠⠊⠀⠀⠀⠀⠸
⢀⠤⠤⢀⡀⠀⠀⢡⠀⢣⡁⠀⢀⠀⠀⠀⠠⠴⠗⡩⠊⠀⢀⠎⠀⠀⠀⠇
⡇⠀⠀⠀⡀⠉⠐⠠⢄⡀⢱⡀⠁⠀⠀⠁⠀⡠⠋⠀⠀⢠⠂⠀⠀⠀⢠⠀
⠡⡀⠀⠀⠈⠂⢄⠀⠀⠈⠙⠠⡀⢀⣤⢀⡔⠁⠀⠀⠀⡆⠀⠀⠀⠀⠎⠀
⠀⠈⢄⠀⠀⠀⠀⠠⡀⠀⠀⠀⠈⣉⣳⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⠊⠀⠀
⠀⠀⠀⠁⢀⠀⠀⠀⠡⡀⠀⠀⠀⠀⠘⠔⠀⠀⠀⠀⢠⠩⠦⢠⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠐⠄⡀⠠⠈⠢⢀⠀⠀⠀⡸⠄⣀⣀⣠⡇⠀⢀⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠈⡗⠖⠊⠀⠀⠀⠀⢦⠘⡶⢻⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣍⡆⣸⠀⠀⠀⠀⠀⠈⠳⣸⠫⠑⠙⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠅⠐⠀⡇⠀⠀⠀⠀⠀⠀⠀⠙⠶⠦⠞⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠦⠶⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢖⠄⣀⢤⢴⣩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡖⡼⡀⣦⡹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐
⡀⠀⠀⠁⠢⢄⠀⠀⠀⠀⠀⢀⡷⣩⠛⢣⡱⣾⠄⠀⠀⠀⠀⠀⢀⠠⠐⠀⠀⠀
⠈⠢⡀⠀⢀⢄⠑⠄⡀⠀⢀⣼⠿⢿⡅⠥⠶⢷⢂⠀⠀⠀⡠⠒⢡⠀⠀⠀⠀⠀
⠀⠀⠀⠩⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⢀⠀⠀⠀⠁⢡⠀⠀⠀⠀⠁⠓⡒⠊⠀⠀
⠀⠀⠀⠀⣂⡀⠀⠀⠀⠀⠙⢤⠄⠂⠁⠁⠒⢠⠔⠁⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀
⠀⠀⠀⠀⠹⡏⠀⠀⠀⠀⠀⠀⢑⡄⢒⠒⡔⠁⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⢁⢸⠀⠀⠀⠀⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠿⠃⠀⠀⠀⠀⠀⢀⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⢀⡤⠚⢄⠀⠀⠀⠀⣠⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣡⠋⠀⠀⠀⢣⠀⠈⠁⠈⢛⠁⠀⠀⠀⠀⠀⠀⠀
    """,
    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠤⣼⣿⠂⠀⠀⠠⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠉⠀⣰⣺⣿⠟⠛⢢⡀⠀⢣⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣾⠃⠀⠀⣽⣿⠃⠀⡞⢁⣿⢶⠋⠚⣿⣠⡀
⠀⠀⠀⠀⢆⠀⢰⠀⠀⠀⢰⣿⣀⡀⣐⣿⡏⠀⣸⣷⣿⣿⢬⠀⠀⣸⠋⠀
⠀⠀⠀⠑⠌⢧⢨⣇⡄⠀⣎⣈⡌⠛⢻⢿⣀⢀⡿⣿⣿⡏⣼⠀⢸⠁⠀⠀
⠀⠀⠀⠱⡄⢢⡷⡆⠷⣾⣼⣯⣿⣧⣼⣏⠻⢾⣷⠀⢻⣷⢸⠀⠈⣆⠀⠀
⠀⠀⠀⠀⠘⡏⢀⠔⠉⠉⢉⣻⡧⢌⣿⣎⠾⠜⠻⢴⣿⣿⣸⠀⠀⢹⠀⠀
⠀⠀⠀⠀⠀⠘⡎⠀⠀⠀⠿⣽⠓⢄⠈⠀⠀⠀⠀⠀⠉⠻⣛⠒⢤⢸⡇⠀
⠀⠀⠀⠀⠀⠀⡟⡆⠀⠀⠸⠘⠄⠘⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⣹⡇⠀
⠀⠀⠀⠀⠀⢀⠀⡟⠆⠀⡐⠃⡄⠁⡆⠀⠀⠀⠀⠐⣶⠒⠒⠒⠋⠋⠀⠀
⠀⠀⠀⠀⠀⠸⡀⠘⡀⠀⠃⠀⡇⠀⠁⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢷⠀⣡⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⢿⣄⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⣠⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠸⡀⠀⠀⠀⠈⣦⡖⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⢇⠀⠀⠀⠀⠇⠀⠀⢀⠔⠹⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⠀⢀⡾⠃⠙⡀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠙⠲⣤⣠⣄⣀⠀⠀
⠐⠉⠀⠀⠀⠀⡿⠀⠀⠀⠱⠀⠀⠀⠀⡐⠁⠀⠀⠀⠀⠑⠣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡌⠁⠀⠀⠀⠀⠆⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡷⢄⣄⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠴⡆
⠀⠀⠰⠀⠀⠑⢑⣄⠀⠀⠀⠀⠀⣨⣿⣇⢀⡀⠀⠀⢀⡀⠄⠂⠋⠀⠀⠀
⠀⢀⠀⠀⠀⠀⠀⣈⡩⠤⠤⠤⠴⠿⠟⠛⠷⠶⢶⣒⠶⠤⣀⡀⠀⠀⠀⠀
    """,
    """
⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠂⠀⣠⡖⠉⠀⠊⣡⠖⢉⣽⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⢷⡤⠔⠈⡿⠀⢠⢃⢞⣡⣴⣟⡟⡹⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠀⠀⠸⡆⠀⢘⡆⠀⣼⣾⣿⣛⠝⣱⣿⠃⠀⠀⡸
⠀⠀⠀⠀⠀⠈⡄⠀⠀⢸⡀⢰⠇⠀⢻⠤⠋⠁⠺⣯⠏⠀⠀⢠⠃
⠀⠀⠀⠀⠀⠀⢠⠀⠀⠈⢣⣾⣶⠀⢸⡄⠠⡤⢡⡍⠀⠀⠀⡌⠀
⠀⠀⠀⠀⠀⠀⠀⠡⡀⠀⠀⠈⡇⢸⣼⠗⣦⣴⠾⠀⠀⠀⣼⠅⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢱⣀⣤⣜⣴⡋⠉⠋⠉⢀⠆⠀⠀⠈⡌⢠⠀
⠀⠀⢀⠠⠐⠀⠉⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢠⣾⡇⢸⠀
⡰⠛⠁⠀⠀⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢀⣾⡟⡟⡇⢸⠃
⠃⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢃⣼⣿⠃⡇⡇⢸⠀
⢧⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⢀⣜⣥⣿⣿⣿⠀⣇⡏⢸⠀
⠈⠣⣀⠀⠀⣀⡵⠢⢄⣀⣀⢤⠔⠒⢹⣿⣿⣿⣿⣿⠰⡟⠀⠀⠀
⠀⠀⠀⠈⠟⢹⡁⠀⠀⠉⠒⠺⠧⠀⡘⢿⣯⣿⣿⡟⢡⡄⡄⠀⠀
⠀⠀⠀⠀⠈⠘⡅⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣼⢁⣦⠀⡅⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠀⠐⢄⠀⠀⠀⠀⠐⣤⣼⣿⣯⣄⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠃⠀⠈⠀⠀⠀⠐⢶⣿⣟⣿⣏⣻⢷⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢼⠀⠀⠀⠀⠀⠀⠀⠀⣽⣾⣿⣿⣋⣈⣱⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⢺⣿⡿⣿⣿⣿⡾⡿⢷⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⢺⡿⣟⡾⣋⡴⠂⣻⣾⡇⠀
⠀⠀⠀⠀⠀⠂⠉⠀⠀⠀⠀⠀⡀⢠⣦⣏⣉⠉⢉⠉⣳⢿⠿⡇⠀
    """,
    """
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠄⣠⣄⣠⡄⣠⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡴⠋⡀⢂⠕⢀⠜⢻⣿⣯⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡜⢀⠎⠔⣁⡴⠁⢀⡇⠀⣿⢥⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢼⢠⣿⢊⣼⠊⡧⠃⡾⡇⠀⣸⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⢆⣇⠎⠙⠛⣧⡾⣁⣱⠀⣏⣧⡄⠀⠀⠀⠀
⠀⢀⣴⣶⣼⣸⣼⡆⠀⠀⢁⣀⣛⣿⣾⣼⣾⣿⡀⠀⠀⠀
⢠⣿⣿⡿⠛⠛⠛⠘⢶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣾⡷⠀⠀
⣿⣿⣿⡄⠀⣠⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⡀⠀
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣅⣀⢲⢰⠀
⠘⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⡿⠿⠿⢿⣿⣿⡇⠀⢉⣷⠀
⠀⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⢁⠀⠀⠀⠈⢻⣿⣦⣥⡏⠀
⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⠀⠀⠀⣸⠟⠉⣀⡇⠀
⠀⠘⢿⣆⠀⠁⠐⠂⠀⡔⠹⠑⠤⢀⣀⣴⢇⡧⣾⠏⡄⠀
⠀⠀⠀⠙⠶⠀⠀⠀⠎⠀⠀⠀⠀⣿⡷⢻⡼⣹⡏⠀⠃⠀
⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢋⠀⢸⠀⡟⡀⢰⠀⠀
⠀⠀⠀⢀⠋⠀⠀⠀⠀⠀⠄⠀⠀⠀⢢⠘⡀⠁⠀⠘⠀⠀
⠀⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢂⠈⠂⠀⠀⠀⠀
⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀
⠀⠀⠎⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀
⠀⣰⠀⠀⠀⠀⠀⠀⠈⢂⠀⠀⢠⠀⠀⠀⢀⠎⣧⠀⠀⠀
⢠⠍⣒⠤⠀⡀⠀⠀⠀⠀⢡⣠⠂⠀⠀⡄⣿⠆⠈⢄⠀⠀
⠁⠠⠁⠉⡒⠒⠨⠀⡒⠠⠄⣇⠀⠀⣌⢠⠀⠱⠀⠈⢆⠢
    """,
    """
⣿⣿⣿⣿⠛⠛⠉⠄⠁⠄⠄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⠄⠄⠐⠄⠄⠄⠄⠄⠄⠄⠠⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢀⡀⠠⠃⡐⡀⠠⣶⠄⠄⢀⣿⣿⣿⣿⣿⣿
⣿⣿⣶⠄⠰⣤⣕⣿⣾⡇⠄⢛⠃⠄⢈⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢀⣻⠟⣻⣿⡇⠄⠧⠄⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣟⢸⣻⣭⡙⢄⢀⠄⠄⠄⠈⢹⣯⣿⣿⣿⣿⣿
⣿⣿⣿⣭⣿⣿⣿⣧⢸⠄⠄⠄⠄⠄⠈⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣼⣿⣿⣿⣽⠘⡄⠄⠄⠄⠄⢀⠸⣿⣿⣿⣿⣿
⡿⣿⣳⣿⣿⣿⣿⣿⠄⠓⠦⠤⠤⠤⠼⢸⣿⣿⣿⣿⣿
⡹⣧⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⢇⣓⣾⣿⣿⣿⣿⣿
⡞⣸⣿⣿⢏⣼⣶⣶⣶⣶⣤⣶⡤⠐⣿⣿⣿⣿⣿⣿⣿
⣯⣽⣛⠅⣾⣿⣿⣿⣿⣿⡽⣿⣧⡸⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡷⠹⠛⠉⠁⠄⠄⠄⠄⠄⠄⠐⠛⠻⣿⣿⣿⣿
⣿⣿⣿⠃⠄⠄⠄⠄⠄⣠⣤⣤⣤⡄⢤⣤⣤⣤⡘⠻⣿
⣿⣿⡟⠄⠄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣆⢻⣿⣿⣿⡎⠝
⣿⡏⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⠐
⣿⡏⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⡟⣼
⣿⡠⠜⣿⣿⣿⣿⣟⡛⠿⠿⠿⠿⠟⠃⠾⠿⢟⡋⢶⣿
⣿⣧⣄⠙⢿⣿⣿⣿⣿⣿⣷⣦⡀⢰⣾⣿⣿⡿⢣⣿⣿
⣿⣿⣿⠂⣷⣶⣬⣭⣭⣭⣭⣵⢰⣴⣤⣤⣶⡾⢐⣿⣿
⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⢃⣼⣿⣿
    """,
]

info = "Telegram: HgAnh_7"

# Danh sách màu chữ ANSI
colors = [
    "\033[1;91m",  # Đỏ nhạt
    "\033[1;92m",  # Xanh lá nhạt
    "\033[1;93m",  # Vàng nhạt
    "\033[1;94m",  # Xanh dương nhạt
    "\033[1;95m",  # Tím nhạt
    "\033[1;96m",  # Xanh ngọc nhạt
]

# Chọn banner và màu sắc ngẫu nhiên
random_banner = random.choice(banners)
random_color = random.choice(colors)

# Đảm bảo màu info khác màu banner
random_color1 = random.choice(colors)
while random_color1 == random_color:
    random_color1 = random.choice(colors)

# Xóa màn hình trước khi hiển thị
os.system("cls" if os.name == "nt" else "clear")

# Hiển thị banner với màu ngẫu nhiên
print(random_color + random_banner + "\033[0m")  # Reset màu về mặc định
print("\033[1;97m╔═══════════════════╗\033[0m")
print("\033[1;97m║\033[0m " + random_color1 + info + "\033[0m" + " \033[1;97m║\033[0m")
print("\033[1;97m╚═══════════════════╝\033[0m")
