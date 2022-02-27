import pandas

interest = pandas.read_csv('data/cpih.csv', index_col='year')

def compound(timeseries, year):
    c = 1.
    for v in timeseries['cpi'].loc[year:]:
        c = c*(1+v/100)
    return c

def cummulative(timeseries, year, salary):
    total = 0.
    c = 1.
    for v in timeseries['cpi'].loc[2009:]:
        c = c*(1+v/100)
        print(c, c*salary-salary)
        total = total + salary*(c-1)
        #print(total)
    return total

if __name__ == '__main__':

    print(compound(interest, 2009))
    print(cummulative(interest, 2016, 40000))
    

