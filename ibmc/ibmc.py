from ibmc.ui.view import MainWindow
from ibmc.core.config import Config

import json

class IBMC:
    def __init__(self):
        self.config = Config()
        self.state = 'initialized'
        print('IBMC initialized')

    def Run(self):
        print('IBMC starting....')
        self.state = 'running'
        self.LoadConf('config.json')
        win = MainWindow(True)
        win.Run()
        print('IBMC started')

    def SaveConf(self, path):
        cf = open(path, 'w')
        dump = json.dumps(self.config.configs, indent=4)
        print(dump)
        cf.write(dump)

    def LoadConf(self, path):
        cf = open(path, 'r')
        self.config.Import(json.loads(cf.read()))

