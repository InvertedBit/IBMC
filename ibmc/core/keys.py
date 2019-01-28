class KeyBindings:
    class __KeyBindings:
        def __init__(self):
            self.config = Config()

    instance = None

    def __new__(cls):
        if not Keybindings.instance:
            Keybindings.instance = KeyBindings.__KeyBindings()
        return Keybindings.instance
    def __getattr__(self, name):
        return getattr(self.instance.config['keys'][name])
