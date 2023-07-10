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
class Mammal(Animal):
    def __init__(self, birthType="alive", appearance="hair or fur",
                 blooded="warm", nurseYoung=True):

        Animal.__init__(self, birthType, appearance, blooded)
        self._nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + "and + {} + that they nurse \
            youngs.format(self.nurseYoung)"
