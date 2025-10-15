# import pyautogui

# pyautogui.moveTo(590, 450)
# pyautogui.click ()

# pyautogui.doubleClick ()


# pyautogui.moveTo (
#     500,
#     500,
#     duration = 2,
#     tween = pyautogui.easeInOutQuad
# )

# import pyautogui

# pyautogui.write ('Hello world!', interval = 0.3)
# pyautogui.press ('enter')

# pyautogui.press ('left', presses = 3)


# with pyautogui.hold ('shift'):
#     pyautogui.press (['left', 'left', 'left'])


# pyautogui.hotkey ('ctrl', 'alt', 'del')

# import pyautogui

# pyautogui.alert (text = 'HTB', title = 'EGGISEGG', button = 'OK')
# pyautogui.confirm (
#     text = 'HTB',
#     title = 'EGGISEGG',
#     buttons = ['Yes', 'No']
# )

# pyautogui.prompt (text = 'TOBASIC', title = 'AUSTRALIAISGOODFORYOU', default = 'NONSENSE')
# pyautogui.password (
#     text = 'HTB',
#     title = 'TOBASIC',
#     default = '399',
#     mask = '*'
# )

import pyautogui
import time

print ('akan menulis di notepad dalam jangka waktu 5 detik')
time.sleep (5)

with open ('kuis.txt', 'r') as file:
    text = file.read ()

pyautogui.write (text, interval = 0.01)


print ('selesai')
















