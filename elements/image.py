from elements.base_element import BaseElement


class Image(BaseElement):
    @property
    def type_of(self) -> str:  # Добавили свойство type_of
        return "image"