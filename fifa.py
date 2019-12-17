import time

keyboard = KeyboardController()
mouse = MouseController()
x = 1

while 1 == 1:
        if x >= 10:
                mouse.press(Button.left)
                mouse.release(Button.left)
                x = 0
        keyboard.press('o')
        keyboard.release('o')
        keyboard.press('m')
        keyboard.release('m')
        time.sleep(2)
        keyboard.press('t')
        keyboard.release('t')
        time.sleep(1)
        keyboard.press('0')
        keyboard.release('0')
        time.sleep(1)
        x += 1

