# -*- coding: utf-8 -*-
"""MATH_kids_learning_select_Level_ver

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cyc6SeLjiqMyBVpDaH21kGdZ2VzYP0PV
"""

import random
import requests
from io import BytesIO
from IPython.display import display, Image, clear_output
import ipywidgets as widgets
from ipywidgets import HBox, VBox
import time

# BOSS資訊字典
level_data = {
    0: {
        "boss_hp": 999,
        "target_range": (1, 27),
        "boss_image_id": "1-XBUkBrmFmi7cMJNY-arFyzI68AJ6VHe",
        "boss_defeated_image_id": "1-XBUkBrmFmi7cMJNY-arFyzI68AJ6VHe"
    },      
    1: {
        "boss_hp": 10,
        "target_range": (3, 5),
        "boss_image_id": "1UYaOy_f2nqNkiq780kDk9a1yq8PAC8Dr",
        "boss_defeated_image_id": "17kn1rBYx89S2Ni6n-U6SbCi0eHjjLXLt"
    },
    2: {
        "boss_hp": 25,
        "target_range": (4, 7),
        "boss_image_id": "1koX9N5WV60TLmX5rGBLsRZ8pHwopnBRc",
        "boss_defeated_image_id": "14UmLCbi4BfTq0EAJGFHhaFw8vmhA4F39"
    },
    3: {
        "boss_hp": 40,
        "target_range": (5, 10),
        "boss_image_id": "18Zx4Jo3b2YATufwDqIUWM4we6QKPrqRu",
        "boss_defeated_image_id": "13LIg1BuN8EatQWbB0nw_HKxhbFTLOpNo"
    },
    4: {
        "boss_hp": 60,
        "target_range": (9, 18),
        "boss_image_id": "1vXjqsjXCiaZCrSy3yOE0UabKYnxOc0xu",
        "boss_defeated_image_id": "1tJWh1GA3R9R8-d1D4YvsyHjprwapFTSO"
    },
    5: {
        "boss_hp": 100,
        "target_range": (11, 21),
        "boss_image_id": "12f7hw7oaeyfhWmZwlSETeF517ntRrP_r",
        "boss_defeated_image_id": "1NRhHVDfmCIzlCcVCvv8rF_OQyEq7YXhS"
    }
}

# 定義數字範圍字典
num_ranges = {
    0: (1, 9),    
    1: (1, 2),
    2: (1, 3),
    3: (1, 4),
    4: (1, 4),
    5: (2, 5),
}

def display_image_from_drive(file_id):
    url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(url)
    image_data = BytesIO(response.content)
    image = Image(image_data.getvalue())
    return image

# 隨機選擇一個等級
L = 0

# 查找BOSS字典並顯示出該等級BOSS資訊
boss_info = level_data[L]


# 動作圖片
heal_image_id = "1u1cE-z9qMW_1xQ9dvWA58gM2UML-Rl77"
attack_image_id = "1eRsD0qbscq2PEq-Yy8jAcEbjUm0fIfua"
win_image_id = "1WTZELt5FJnsGGPsavCuhQFZPYxA_OEK9"

heal_image = display_image_from_drive(heal_image_id)
attack_image = display_image_from_drive(attack_image_id)

heal_image_widget = widgets.Image(value=heal_image.data, layout=widgets.Layout(visibility="hidden"))
attack_image_widget = widgets.Image(value=attack_image.data, layout=widgets.Layout(visibility="hidden"))

win_image = display_image_from_drive(win_image_id)
win_image_widget = widgets.Image(value=win_image.data, layout=widgets.Layout(width='120px', height='120px'))

# 勝利動畫圖片
win_electric_icon01_file_id = "1tuXpwJvUF32aocoVGiIb3ON4dnHd9GfL"
win_electric_icon02_file_id = "1vKLgY9qQB8RUfQbmZiur5y5iqAJu3uc-"
win_electric_icon03_file_id = "1J2Q_0vIeN6RVHcsMPEAsCcZJZz6oojCP"

win_electric_icon01_image = display_image_from_drive(win_electric_icon01_file_id)
win_electric_icon01_widget = widgets.Image(value=win_electric_icon01_image.data)

win_electric_icon02_image = display_image_from_drive(win_electric_icon02_file_id)
win_electric_icon02_widget = widgets.Image(value=win_electric_icon02_image.data)

win_electric_icon03_image = display_image_from_drive(win_electric_icon03_file_id)
win_electric_icon03_widget = widgets.Image(value=win_electric_icon03_image.data)

# 顯示BOSS圖片
boss_image = display_image_from_drive(boss_info['boss_image_id'])
boss_defeated_image = display_image_from_drive(boss_info["boss_defeated_image_id"])
boss_image_widget = widgets.Image(value=boss_image.data)
boss_defeated_image_widget = widgets.Image(value=boss_defeated_image.data)


# 創建五個按鈕以指定招喚L 1〜5的BOSS
level_button_layout = widgets.Layout(width='75px', height='40px', background_color='#ADD8E6')

def on_level_button_click(btn):
    global L
    L = int(btn.description)
    restart_game(None)  # 調用 restart_game 來更新關卡
    # 更新BOSS圖片
    boss_info = level_data[L]
    boss_image_id = boss_info["boss_image_id"]
    boss_image = display_image_from_drive(boss_image_id)
    boss_image_widget.value = boss_image.data
    boss_image_container.children = (boss_image_widget,)

level_buttons = [widgets.Button(description=str(i), layout=level_button_layout) for i in range(1, 6)]
for btn in level_buttons:
    btn.on_click(lambda btn: on_level_button_click(btn))

level_buttons_box = widgets.HBox(level_buttons)


# 在最上方顯示創建的等級按鈕
display(level_buttons_box)

# 創建一個包含boss_image_widget的容器並顯示
boss_image_container = widgets.VBox([boss_image_widget], layout=widgets.Layout(width='402px', height='402px'))
display(boss_image_container)


# 從範圍中隨機選擇數字
nums = [random.randint(*num_ranges[L]) for _ in range(9)]

# 定義按鈕點擊事件函數
def on_button_clicked(btn):
    global s, present
    btn.disabled = True
    s += int(btn.description)
    present_box.value = s

def flash_image(image_widget, duration=1):
    image_widget.layout.visibility = "visible"
    time.sleep(duration)
    image_widget.layout.visibility = "hidden"

# 確認按鈕, 清空 present 變量的函數
def reset_present():

    for btn in buttons:
        btn.description = str(random.randint(1, 3))
        btn.disabled = False

    global boss_hp, target, winner, target_range
    # 判斷 BOSS_HP 大於 0
    if boss_hp > 0 and present_box.value == target_box.value:
        boss_hp -= present_box.value
        boss_hp_box.value = boss_hp
        flash_image(attack_image_widget)
    else:
        boss_hp += 1
        boss_hp_box.value = boss_hp
        flash_image(heal_image_widget)

    # 判斷 BOSS_HP 是否小於等於 0   
    if boss_hp <= 0:
        # 無效化 confirm按鈕
        confirm_btn.disabled = True

        # 顯示動畫效果
        boss_image_container.children = (win_electric_icon01_widget,)
        time.sleep(2)
        boss_image_container.children = (win_electric_icon02_widget,)
        time.sleep(1)
        boss_image_container.children = (win_electric_icon03_widget,)
        time.sleep(1)

        # 移除動畫效果並添加boss_defeated_image_id
        boss_defeated_image_id = level_data[L]["boss_defeated_image_id"]
        display_image_from_drive(boss_defeated_image_id)
        boss_image_container.children = (boss_defeated_image_widget,)

        # 顯示 Winner
        winner = winner_hbox
        display(winner)

        # 啟用 Restart 按鈕
        restart_button.disabled = False
    if boss_hp != boss_hp - target:  # 判斷 boss_hp 是否有變化
        target = random.randint(*target_range)  # 重新產生一個隨機數作為新的 target
        target_box.value = target    
    # 重置 present 和按鈕的數字    
    global s, present
    s = 0
    present = s
    present_box.value = s 
 
           
  
# 定義restart_game 函数
def restart_game(btn):
    global boss_hp, target, winner, L, target_range, nums

    # 恢復 BOSS 血量
    boss_hp = level_data[L]["boss_hp"]
    boss_hp_box.value = boss_hp

    # 更新目標數字
    target_range = level_data[L]["target_range"]
    target = random.randint(*target_range)
    target_box.value = target

    # 重置 present 和按鈕的數字
    global s
    s = 0
    present_box.value = str(s)
    for btn in buttons:    
        btn.description = str(random.randint(1, 3)) 
        btn.disabled = False      

    # 移除 Winner
    if winner:
        winner.layout.visibility = "hidden"
    
    # 隱藏 Restart 按鈕
    btn.disabled = True

    # 顯示 BOSS 圖片
    boss_image_id = level_data[L]["boss_image_id"]
    display_image_from_drive(boss_image_id)
    boss_image_container.children = (boss_image_widget,)    

    # 重置數字範圍
    num_range = num_ranges[L]
    nums = [random.randint(*num_range) for _ in range(9)]

    # 更新等級資訊
    boss_info = level_data[L]

    # 隨機顯示數字
    for i in range(len(nums)):
        buttons[i].description = str(nums[i])
        buttons[i].disabled = False
    # 無效化 confirm按鈕
    confirm_btn.disabled = False        



# 初始化
boss_hp = level_data[L]["boss_hp"]
target_range = level_data[L]["target_range"]
target = random.randint(*target_range)
s = 0
present = s
winner = None


# 產生按鈕
button_layout = widgets.Layout(width='120px', height='42px')
buttons = [widgets.Button(description=str(num), layout=button_layout) for num in nums]


# 將按鈕放入 3x3 的網格中
grid = widgets.GridBox(buttons, layout=widgets.Layout(grid_template_columns="repeat(3,125px)", grid_template_rows="repeat(3,45px)"))

# 綁定按鈕點擊事件
for btn in buttons:
    btn.on_click(lambda btn: on_button_clicked(btn))

# 設定以下BOX大小
box_layout = widgets.Layout(width='198px', height='30px', justify_content='center', align_items='center')
# 顯示 BOSS HP
boss_hp_box = widgets.IntText(value=boss_hp, description="BOSS HP", layout=box_layout)
# 顯示 Target
target_box = widgets.IntText(value=target, description="Target", layout=box_layout)
# 顯示 Present
present_box = widgets.IntText(value=present, description="Present", layout=box_layout)
# 將 BOSS HP、Target 和 Present放在一個垂直方向的容器中
boss_hp_target_present_vbox = widgets.VBox([boss_hp_box, target_box, present_box])
# 將治療和打擊圖片放在一個水平方向的容器中
heal_attack_hbox = widgets.HBox([heal_image_widget, attack_image_widget], layout=widgets.Layout(width='200px', height='100px'))

# 將兩個容器放在一個水平方向的容器中並顯示
boss_hp_target_present_heal_attack_hbox = widgets.HBox([boss_hp_target_present_vbox, heal_attack_hbox])
display(boss_hp_target_present_heal_attack_hbox)
# 產生確認按鈕
confirm_btn = widgets.Button(description="確認送出")
confirm_btn.on_click(lambda btn: reset_present())

# 將按鈕和清空按鈕、BOSS血量方塊放入布局中
buttons_layout = widgets.VBox([grid])
display(widgets.HBox([buttons_layout,]))

# 創建 Restart 按鈕
restart_button = widgets.Button(description="Restart", layout=widgets.Layout(visibility="visible"), disabled=True)

# 綁定 Restart 按鈕點擊事件
restart_button.on_click(restart_game)

# 將 Confirm 按鈕和 Restart 按鈕放在一個水平方向的容器中 # 顯示水平方向的容器
confirm_restart_hbox = widgets.HBox([confirm_btn, restart_button])
display(confirm_restart_hbox)




#顯示WINNER BOX
winner_hbox = HBox([win_image_widget,])