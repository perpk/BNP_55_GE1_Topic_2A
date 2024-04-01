import unittest
from sample.is_leap_year import is_leap_year

LEAP_YEARS = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

class IsLeapYearTestCase(unittest.TestCase):
    def testLeapYear(self):
        for year in LEAP_YEARS:
            assert is_leap_year(year) == True

    def testNotLeapYear(self):
        for year in range(1900, 2020):
            if year in LEAP_YEARS:
                continue
            assert is_leap_year(year) == False