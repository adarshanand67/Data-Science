# Python code showing all the ratios together,
# make sure you have installed fuzzywuzzy module

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# for process library,
choices = ['geek for geek', 'geek geek', 'g. for geeks']
query = 'geeks for geeks'
print( "List of ratios: ")
print( process.extract(query, choices), '\n')
print( "Best among the above list: ",process.extractOne(query, choices))

# Use cases?

# Use fuzzywuzzy to find the best match for a given query string if user input is not exact
