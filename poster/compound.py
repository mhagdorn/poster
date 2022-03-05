__all__ = ['pay_loss', 'cummulative']

from pathlib import Path
import pandas


cpi_pay = pandas.read_csv(
    Path('data', 'inflation_pay.csv'), index_col='year')


def compound(ts):
    c = 1.
    for rate in ts:
        c = c * (1 + rate / 100)
    return c


cum_pay = compound(cpi_pay['pay_increase'].loc[2009:])
cum_inflation = compound(cpi_pay['rpi'].loc[2009:])
pay_loss = (cum_inflation / cum_pay - 1) * 100


def check_year(year):
    return min(max(year, 2009), 2020)


def cummulative(year, salary):
    year = check_year(year)
    # reduce todays salary by previous pay rises
    salary = salary / cum_pay
    c = 1.
    p = 1.
    total = 0.
    for y, d in cpi_pay.iterrows():
        c = c * (1 + d['rpi'] / 100)
        p = p * (1 + d['pay_increase'] / 100)
        if y >= year:
            total += (c - p) * salary
    return total


if __name__ == '__main__':
    print(pay_loss)
    print(cummulative(2009, 40000))
