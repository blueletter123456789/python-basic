import requests


class ThirdPartyBonusRestApi(object):
    def bonus_price(self, year):
        r = requests.get('https://localhost/get', params={'year': year})
        return r.json()['price']


class Salary(object):
    def __init__(self, base=100, year=2017):
        self.bonus_api = ThirdPartyBonusRestApi()
        self.base = base
        self.year = year

    def calculation_salary(self):
        bonus = self.bonus_api.bonus_price()
        return self.base + bonus
