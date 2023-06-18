import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 54, 24) == 30

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 7) == 14

    def test_division_succes(self):
        assert  self.calc.division(self, 1000, 100) == 10

    def teardown(self):
        print('Выполнение метода Teardown')
