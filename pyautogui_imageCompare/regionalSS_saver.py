import pyautogui

im1 = pyautogui.screenshot(region=(5,150,180,270))
im1.save(r"./savedimage.png")