# A
## i.
from hours_since_end_2022 import hours_since_end_2022
from is_leap_year import is_leap_year

protein = input("Please enter a protein...")
year_of_discovery = int(input("Now please enter the year when the protein was discovered..."))

known_for_hours = hours_since_end_2022(year_of_discovery)
print(f"The protein {protein} is known for {known_for_hours} hours since the end of 2022")

## ii.
leap_year = is_leap_year(year_of_discovery)
text_leap_year = "a"
if not leap_year:
    text_leap_year = "not a"

print(f"The year of the discovery is {text_leap_year} leap year")
