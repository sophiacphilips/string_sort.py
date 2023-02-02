#Name: Sophia Philips
#GithubUsername: sophiacphilips
#Date: 01/31/23
#This code is designed to take a list of string and sort them alphabetically using the
#insertion sort algorithm.



def string_sort(string_list):
  """
  Sorts a list of strings in alphabetical order.
  """
  for index in range(1, len(string_list)):
    letter = string_list[index]
    pos = index - 1
    while pos >= 0 and string_list[pos].lower() > letter.lower(): #".lower" changes strings to all lower case so they can be sorted alphabetically without case influence
      string_list[pos + 1] = string_list[pos]
      pos -= 1
    string_list[pos + 1] = letter




