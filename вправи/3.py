def years(years_list):
    print(f"Мені виповнилося 3 роки у {years_list[3]}")
    years_list.append(2013)
    print(years_list)
    print(f"Найбільше років мені було у {years_list[-1]}")
years([2007,2008,2009,2010,2011,2012])