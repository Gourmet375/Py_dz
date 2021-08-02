from abc import ABC, abstractmethod


class Clothes(ABC):
    expense_count = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expense_count += self.expense

    def __str__(self):
        return f'Пальто: размер {self.size}, раход ткани {self.expense}, общий расход ткани {Coat.expense_count:.02f}'

    @property
    def expense(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Costume.expense_count += self.expense

    def __str__(self):
        return f'Костюм: рост {self.height}, расход ткани {self.expense}, общий расход ткани {Costume.expense_count:.02f}'

    @property
    def expense(self):
        exp = (self.height * 2 + 0.3) / 100
        return float(f'{exp:.02f}')


cloth_1 = Coat(55)
print(cloth_1)
cloth_2 = Coat(45)
print(cloth_2)
cloth_3 = Costume(185)
print(cloth_3)
cloth_4 = Costume(174)
print(cloth_4)
