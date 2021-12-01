class Color:
    color_name: str = "неизвестный цвет"
 
    def name(self) -> str:
        return self.color_name
 
 
class Green(Color):
    color_name = "зелёный"
 
 
class Yellow(Color):
    color_name = "жёлтый"


class Kind:
    kind_name: str = "неизвестная форма"
 
    def name(self) -> str:
        return self.kind_name
 
 
class Smooth(Kind):
    kind_name = "гладкий"
 
 
class Brain(Kind):
    kind_name = "мозговой"

class Peas:
 
    color: Color
    kind: Kind
 
    def __init__(self, color: Color, kind: Kind):
        self.color = color
        self.kind = kind
 
    def __str__(self):
        return f"{self.color.name().capitalize()} {self.kind.name()} горошек."
    

    

