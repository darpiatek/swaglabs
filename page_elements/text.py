from .element import Element


class TextElement(Element):

    @property
    def value(self):
        return self.element.text
