from app.classes.client import Client
from app.classes.window import Window
from datetime import datetime
from app.main import WINDOWS_NAVES
from app.constants.prices import GLASS_TYPE_PRICES, ALUMINUM_STYLE_PRICES


class Order:
    def __init__(self, id: str, client: Client, date: datetime) -> None:
        self.id = id
        self.client = client
        self.date = date
        self.windows: list[Window] = []
        self.discount_applied = False
        self.total = 0.00

    def add_window(
        self, width: int, height: int, style: int, glass_t: int, aluminum_s: int
    ) -> None:
        window_naves = WINDOWS_NAVES[style - 1]
        glass_type = GLASS_TYPE_PRICES[glass_t - 1]
        aluminum_style = ALUMINUM_STYLE_PRICES[aluminum_s - 1]

        if window_naves.validate_size(width, height):
            window = Window(
                width,
                height,
                window_naves.count_chapas(),
                window_naves.count_naves(),
                glass_type,
                aluminum_style,
            )
            self.windows.append(window)

            price = window.calculate_price()
            self.total += price

        return

    def apply_discount(self) -> None:
        if not self.discount_applied and len(self.windows) >= 100:
            self.total = self.total * 0.9

        return
