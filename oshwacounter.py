#python3

import csv
import collections

#turns the csv into a list of lists [[x, y, z,], [a, b, c]]
exampleFile = open('oshwa-9-30-2020.csv')
exampleReader = csv.reader(exampleFile)
oshwadata = list(exampleReader)
#removes the header
del oshwadata[0]


#list to hold all of the countries for counting purposes
country_counter_list = []
entity_counter_list = []

#work through the list to pull the data
for row in oshwadata:

    #add the country to the list for future counting
    country_counter_list.append(row[4])

    #add the entity to the list for future counting
    entity_counter_list.append(row[2])

#creates a dictionary with country as key and number of occurances as value
country_counter = collections.Counter(country_counter_list)
print(country_counter)

#creates a dictionary with an entity as a key and a number of occurances as a value
entity_counter = collections.Counter(entity_counter_list)
print(entity_counter)

#writes a csv with the countries in one column and the counts in the next column
with open('oshwa_country_list.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(country_counter.items())

#writes a csv with the entities in one column and the counts in the next column
with open('oshwa_entity_list.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(entity_counter.items())
