from nose.plugins import Plugin


class AchievementsPlugin(Plugin):
    name = 'achievements'

    def __init__(self, achievements=None, data=None):
        Plugin.__init__(self)
        if data is None:
            data = {}
        self.data = data
        self.achievements = achievements

    def options(self, parser, env):
        Plugin.options(self, parser, env)
    
    def configure(self, options, conf):
        Plugin.configure(self, options, conf)

