# -*- coding: utf-8 -*-

class Achievement(object):
    template = """
  /.–==*==–.\\
 ( |      #| ) %(announcement)s
  ):      ':(
    `·…_…·´    %(title)s
      `H´      %(subtitle)s
     _.U._     %(message)s
    [_____]"""
    title = None
    subtitle = None
    message = None

    def configure(self, options, conf):
        pass
    
    def finalize(self, data, result):
        pass

    def announcement(self, info=None):
        template = self.template
        try:
            template = template.decode('utf-8')
        except AttributeError:
            pass
        return template % {'announcement': "Achievement unlocked!",
                           'title': self.title or "",
                           'subtitle': self.subtitle or "",
                           'message': self.message or ""}

