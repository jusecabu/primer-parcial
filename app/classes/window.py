from app.constants.prices import CORNER_PRICE, CHAPAS_PRICE


class Window:
    def __init__(
        self,
        width: int,
        height: int,
        chapas: int,
        naves: int,
        glass_type: float,
        aluminum_style: float,
    ) -> None:
        self.width = width
        self.height = height
        self.naves = naves
        self.chapas = chapas
        self.x_side = (width / naves) - 6
        self.y_side = height - 6
        self.glass_area = (self.x_side + 3) * (self.y_side + 3)
        self.glass_type = glass_type
        self.aluminum_style = aluminum_style

    def calculate_price(self) -> float:
        glass_price = self.glass_type * self.glass_area
        aluminum_price = self.aluminum_style * ((self.x_side * 2) + (self.y_side * 2))
        corners_price = CORNER_PRICE * 4
        chapas_price = 0.00

        if self.chapas > 0:
            chapas_price = CHAPAS_PRICE * self.chapas

        total = (
            glass_price + aluminum_price + corners_price + chapas_price
        ) * self.naves

        return total
