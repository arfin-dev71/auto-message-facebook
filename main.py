from email import message
import pyautogui
import time
message = 5
while message > 0:
  time.sleep (4)
  pyautogui.typewrite('i miss you')
  time.sleep(2)
  pyautogui.press('enter')
  message = message - 1
  