class Hyperlink:
    def __init__(self, title: str, href: str, obj: str):
        self.title: str = title
        self.href: str = href
        self.obj: str = obj

    def getFullWikiLink(self) -> str:
        return f"https://en.wikipedia.org{self.href}"

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and getattr(other, "href", None) == self.href
        )

    def __hash__(self):
        return hash(self.title + self.href)

    def __str__(self):
        return f"{self.title} ({self.getFullWikiLink()})"
