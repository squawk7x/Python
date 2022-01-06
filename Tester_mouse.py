from pynput import mouse   
import keyboard
   
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('left')
        keyboard.press_and_release
    
    if button == mouse.Button.middle:
        print('middle')
        keyboard.send('space')

    if button == mouse.Button.right:
        print('right')
        #keyboard.send('alt')
    
def on_scroll(x, y, dx, dy):
    print('scroll')
    #keyboard.send('tab')

with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()