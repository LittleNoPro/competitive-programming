import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis = 0))        #Output : [4 6]
print(numpy.sum(my_array, axis = 1))        #Output : [3 7]
print(numpy.sum(my_array, axis = None))      #Output : 10
print(numpy.sum(my_array))                   #Output : 10




import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.prod(my_array, axis = 0))            #Output : [3 8]
print(numpy.prod(my_array, axis = 1))            #Output : [2 12]
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24




import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0




import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7