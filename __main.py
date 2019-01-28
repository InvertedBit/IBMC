from pyglet.window import Window, key
from pyglet.text import Label
from pyglet import app


texts = ['Movies', 'TV', 'Music', 'Options']
index = 0
maxIndex = 3

mainWindow = Window(fullscreen=True)
label = Label(texts[index], font_name='Monospace', font_size=24, x=mainWindow.width//2, y=mainWindow.height//2, anchor_x='center', anchor_y='center')



@mainWindow.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        if index == maxIndex:
            index = 0
        else:
            index += 1
    elif symbol == key.DOWN:
        if index == 0:
            index = maxIndex
        else:
            index -= 1

    label.text = texts[index]

@mainWindow.event
def on_draw():
    mainWindow.clear()
    label.draw()

app.run()
