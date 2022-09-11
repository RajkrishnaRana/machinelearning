import pyautogui
import time
import webbrowser as wb
wb.open ("web.whatsapp.com")
time.sleep(10)
for i in range (10):
    pyautogui.press ("h")
    pyautogui.press ("i")
    pyautogui.press ("enter")
    pyautogui.press ("h")
