import unittest

from main import CaloriesCalculator, CashCalculator, r1, r2, r3, r4, r5

class TestLB3(unittest.TestCase):

    def test_CaloriesCalculator(self):
        calories_calculator = CaloriesCalculator(2000)
        calories_calculator.add_record(r4)
        calories_calculator.add_record(r5)
        self.assertEqual(calories_calculator.get_calories_remained(),
                         'Вы можете потребить ещё 1150 калорий')

    def test_CashCalculator(self):
        cash_calculator = CashCalculator(2000)
        cash_calculator.add_record(r1)
        cash_calculator.add_record(r2)
        cash_calculator.add_record(r3)
        self.assertEqual(cash_calculator.get_today_cash_remained('rub'), 'Ваш долг - 345.0 руб')

    def test_extra(self):
        calories_calculator = CaloriesCalculator(2000)
        calories_calculator.add_record(r4)
        self.assertEqual(calories_calculator.get_today_limit_balance(), 1750)

if __name__ == '__main__':
    unittest.main()