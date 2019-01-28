class Config:

    class __Config:
    
        def __init__(self):
            self.configs = {}

        def Import(self, configs):
            self.configs = configs

        def __getattr__(self, name):
            if not self.configs[name]:
                return ''
            return self.configs[name]

        
    instance = None

    def __new__(cls):
        if not Config.instance:
            Config.instance = Config.__Config()
        return Config.instance    
    def __getattr__(self, name):
        return getattr(self.instance.configs[name])

