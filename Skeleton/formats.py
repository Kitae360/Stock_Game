import re

def all_integer_correct_format(string):
	return string_match_format(string) and check_time_all_integers(string)


def string_match_format(string):
  if re.match('\d\d\d\d-\d\d\-\d\d', string):
	return True
  else:
	return False

def check_time_all_integers(string):
  list_of_integers = string.split("-")
  year = list_of_integers[0]
  month = list_of_integers[1]
  day = list_of_integers[2]
  return year.isdigit() and month.isdigit() and day.isdigit()

