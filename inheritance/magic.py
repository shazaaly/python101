class Animal:
    def __init__(self, birthType="unknown", appearance="unknown", blooded="unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} and is {}, also is {}.format(type(self).__name__, \
            self.birthType, self.blooded, self.appearance)"

# inherir all

