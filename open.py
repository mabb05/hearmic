import pyautogui as p

p.hotkey('win','d')
p.sleep(1)
p.rightClick(p.locateCenterOnScreen('icon.png',confidence=0.9))
p.press('up');  p.press('up')
p.press('enter')

p.sleep(0.8)
p.click(p.locateCenterOnScreen('recording.png',confidence=0.9))
p.sleep(0.1)
p.click(p.locateCenterOnScreen('mic.png',confidence=0.9))
p.sleep(0.1)
p.click(p.locateCenterOnScreen('prop.png',confidence=0.9))
p.sleep(0.1)
p.click(p.locateCenterOnScreen('listen.png',confidence=0.9))
p.sleep(0.1)
p.click(p.locateCenterOnScreen('yeslisten.png',confidence=0.9))
p.sleep(0.1)
p.click(p.locateCenterOnScreen('apply.png',confidence=0.9))

p.sleep(0.1)
p.press('esc')
p.press('esc')
