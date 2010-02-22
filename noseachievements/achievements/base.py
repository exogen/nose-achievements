# -*- coding: utf-8 -*-

class Achievement(object):
    template = u"""
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
        return self.template % {'announcement': "Achievement unlocked!",
                                'title': self.title or "",
                                'subtitle': self.subtitle or "",
                                'message': self.message or ""}

