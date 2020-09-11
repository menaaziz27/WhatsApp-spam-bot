import webbrowser
import pyautogui
import time
import cv2
#def spammer(word):
webbrowser.open('https://web.whatsapp.com/')
time.sleep(8)
pyautogui.click(pyautogui.locateOnScreen('E:\\code\\mypythonscripts\\whatsapp gena\\spam\\search.PNG' , grayscale=True, confidence=.9) , duration = .5)
pyautogui.write('kero youssef' , interval = 0.1)
#pyautogui.moveRel(0 , 60 , duration = 0.5)
pyautogui.press('enter')
pyautogui.click(pyautogui.locateOnScreen('E:\\code\\mypythonscripts\\whatsapp gena\\type.PNG', grayscale=True, confidence=.6) , duration = 1)
pyautogui.click(pyautogui.moveTo(580,647,0.5))
for i in range(10):
	pyautogui.write('This is a spam bot being testing!' , interval=0.0)
	pyautogui.press('enter')
#spammer('Hi')
