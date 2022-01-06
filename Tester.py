'''
# #stats = {'a':1000, 'b':3000, 'c': 100}

#inverse = [(value, key) for key, value in stats.items()]
#print max(inverse)[1]
player_list = [('P-1', 60), ('P-2', 20), ('P-3', 40)]
print(player_list)

print(sorted(player_list, key=lambda player: player[1]))
print(player_list)

print(max(player_list))

'''


import keyboard
from pynput import mouse


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('left')
        keyboard.send('shift')

    if button == mouse.Button.middle:
        print('middle')
        keyboard.send('space')

    if button == mouse.Button.right:
        print('right')
        keyboard.send('alt')
    
def on_scroll(x, y, dx, dy):
    print('scroll')
    keyboard.send('tab')

with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()





