class Moon(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


moon1 = Moon()
print(id(moon1))
moon2 = Moon()
print(id(moon2))
