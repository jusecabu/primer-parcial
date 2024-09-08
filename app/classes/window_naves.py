class WindowNaves:
    def __init__(self, nave_type: str) -> None:
        self.nave_type = nave_type

    def validate_size(self, width: int, height: int) -> bool:
        naves = len(list(self.nave_type))

        if height < 8 or width < 8 * naves:
            return False

        return True

    def count_chapas(self) -> int:
        x_naves = self.nave_type.lower().count("x")

        return x_naves

    def count_naves(self) -> int:
        naves = len(list(self.nave_type))

        return naves
