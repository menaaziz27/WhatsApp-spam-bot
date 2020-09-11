import webbrowser
import pyautogui
import time
import cv2

webbrowser.open('https://web.whatsapp.com/')
time.sleep(8)
pyautogui.click(pyautogui.locateOnScreen('string\\path\\location\\to\\search.PNG' , grayscale=True, confidence=.9) , duration = .5)

#here add which contact phone name you want to spam and hit enter key
pyautogui.write('' , interval = 0.1)
pyautogui.press('enter')

#move mouse cursor to the chat field
#pyautogui.click(pyautogui.locateOnScreen('string\\path\\location\\to\\type.PNG', grayscale=True, confidence=.6) , duration = 1)

#another way to specify the x and y points of the chat field in your screen
#it depends on your screen 
pyautogui.click(pyautogui.moveTo(580,647,0.5))
for i in range(10):
	pyautogui.write('This is a spam bot being testing!' , interval=0.0)
	pyautogui.press('enter')

