from pyglet.window import Window, key
from pyglet.text import Label
from pyglet import app
from pyglet import media

import vlc

from ibmc.core.config import Config

class MainWindow:
    def __init__(self,fullscreen):
        self.fullscreen = fullscreen
        self.config = Config()
        self.Instance = vlc.Instance();
        self.player = self.Instance.media_player_new()
        media = self.Instance.media_new(self.config.configs['playlist'][1])
        self.player.set_media(media)
        #self.player = media.Player()
        #track = media.load(self.config.configs['playlist'][1])
        #self.player.queue(track)
        self.texts = ['Movies', 'TV', 'Music', 'Options']
        self.index = 0
        self.maxIndex = 3
        self.mainWindow = Window(fullscreen=self.fullscreen)
        self.label = Label(self.config.ui['greeting'], font_name='Monospace', font_size=24, x=self.mainWindow.width//2, y=self.mainWindow.height//2, anchor_x='center', anchor_y='center')

        
        @self.mainWindow.event
        def on_draw():
            self.mainWindow.clear()
            self.label.draw()
        #    if self.player.get_texture():
        #        self.player.get_texture().blit(0, 0)

        @self.mainWindow.event
        def on_key_press(symbol, modifiers):
            if symbol == key.UP:
                if self.index == self.maxIndex:
                    self.index = 0
                else:
                    self.index += 1
            elif symbol == key.DOWN:
                if self.index == 0:
                    self.index = self.maxIndex
                else:
                    self.index -= 1
            elif symbol == key.SPACE:
                #self.player = vlc.MediaPlayer(self.config.configs['playlist'][1])
                #self.player.play()
                self.player.set_xwindow(self.GetHandle())
                self.player.play()

            elif symbol == key.RETURN:
                self.player.pause()

            self.label.text = self.texts[self.index]

    def Run(self):
        app.run()
    
