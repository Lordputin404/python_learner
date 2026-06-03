# default arguments = a default value for certain parameters
#                  default is used when thar argument is ommited
#                  make functions more flexible reduces numbers
#                  of arguments 1. positional 2. DEFAULT 3. keyword
#                  4. orbitrary

def area_circle(radius, pie=3.14):
    return pie * radius*radius

print(area_circle(4))