from meiga import Result, Error, Success, isFailure


class DummyCalculator:
    def __init__(self, number_1: int, number_2: int):
        self.number_1 = number_1
        self.number_2 = number_2

    def sum(self) -> Result[Error, int]:
        return Success(self.number_1 + self.number_2)

    def sub(self) -> Result[Error, int]:
        return Success(self.number_1 - self.number_2)

    def divide(self) -> Result[Error, float]:
        if self.number_2 != 0:
            return Success(float(self.number_1) / float(self.number_2))
        else:
            return isFailure
