
class Article:
    def __init__(self, _title, _content):
        self._title = _title
        self._content = _content

    @property
    def art_cont(self):
        return self._content

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title


art1 = Article("intro to C", "Lorem Ipsum")   # use getter to access private
print(art1.art_cont)

art1.title = "Intro to JAvaScript"  # change attr prop via setter
print(art1.title)
