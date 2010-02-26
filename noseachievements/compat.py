try:
    basestring = basestring
except NameError:
    basestring = str

try:
    unicode = unicode
except NameError:
    unicode = str

try:
    callable = callable
except NameError:
    def callable(obj):
        return hasattr(obj, '__call__')

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    import cPickle as pickle
except ImportError:
    import pickle

