import random
import time

import memory_profiler as mem_profile

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print('Memory (Before): {}Mb '.format(mem_profile.memory_usage_psutil()))
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

def people_list(num_people):
    ''' Generate people list using a list '''
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    ''' Generate people list using a generator '''
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.time()
people = people_list(1000000)
t2 = time.time()

# t1 = time.time()
# people = people_generator(1000000)
# t2 = time.time()

print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

print ('Took ' + str(t2-t1) + ' Seconds')
