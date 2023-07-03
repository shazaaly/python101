class Campaign:
    def __init__(self, _type, duration, __premium):
        self._type = _type  # Assigning _type to a class attribute
        self.duration = duration
        self.__premium = __premium


AddidasCamp = Campaign("commercial", 5, True)
print(AddidasCamp._type)
print(AddidasCamp.duration)
# AttributeError: 'Campaign' object has no attribute '__premium':
print(AddidasCamp.__premium)


class Ad(Campaign):
    def __init__(self, _type, duration, __premium):
        super().__init__(_type, duration, __premium)


NikeAd = Ad("commercial", 9, False)
print(NikeAd._type)
print(NikeAd.duration)
print(NikeAd.__premium)
