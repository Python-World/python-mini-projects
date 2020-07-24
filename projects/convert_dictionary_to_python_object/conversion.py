class obj(object):
    def __init__(self, d):
        for x, y in d.items():
            setattr(self, x, obj(y) if isinstance(y, dict) else y)
data = {'a':5,'b':7,'c':{'d':8}}
ob = obj(data)
