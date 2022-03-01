import pandas

interest = pandas.read_csv('data\cpi_and_pay_increases.csv', index_col='year')

def compound(timeseries, year):
    c = 1.
    for v in timeseries['cpi'].loc[year:]:
        c = c*(1+v/100)
    return c

def cummulative(timeseries, year, salary):
    total = 0.
    c = 1.
    adj_salary = []
    salary_diff = []
    timeseries = timeseries.sort_values(by=['year'])
    #timeseries = timeseries.sort_values(by=['year']).loc[year:]
    for index, row in timeseries.iterrows():
        c = c*(1+row['cpi']/100)
        print(c, c*salary-salary)
        adj_salary.append(salary*(1+row['pay_increase']/100))
        salary_diff.append(salary*(c-1))
    timeseries['salary_diff'] = salary_diff
    timeseries['adj_salary'] = adj_salary
    total = timeseries.loc[year:]['salary_diff'].sum()
    return total

if __name__ == '__main__':

    print(compound(interest, 2009))
    print(cummulative(interest, 2011, 40000))
    

