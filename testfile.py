import numpy as np
import pandas as pd


start_year = 1936
end_year = 2022
full_years = range(start_year,end_year+1)
omit_years = [1940, 1941, 1943, 1944, 1957, 1959, 1961, 1963, 1965]
year_list = [x for x in full_years if x not in omit_years]




for year in year_list:
    print(year)


