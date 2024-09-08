from app.classes.client import Client
from app.classes.order import Order


class App:
    def __init__(self) -> None:
        self.clients: list[Client] = []
        self.orders: list[Order] = []
