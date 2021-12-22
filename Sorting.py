'''
SORTING


'''

'''
EXAMPLE 1

list.sort() changes the list
'''
# Alkaline earth metals

earth_metals = ["Berylium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
print(earth_metals)
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse=True)
print(earth_metals)

earth_metals = ("Berylium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
# earth_metals.sort()

'''
EXAMPLE 2

'''

# format := (name, radius, density, distance from Sun)
planets = [
	("Mercury", 2440, 5.43, 0.395),
	("Venus", 6052, 5.24, 0.723),
	("Earth", 6378, 5.52, 1.000),
	("Mars", 3396, 3.93, 1.530),
	("Jupiter", 71492, 1.33, 5.210),
	("Saturn", 60268, 0.69, 9.551),
	("Uranus", 25559, 1.27, 19.213),
	("Neptune", 24764, 1.64, 30.070)
]

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)

density = lambda planet: planet[2]
planets.sort(key=density)
print(planets)

'''
EXAMPLE 3 - sorted()


built-in function sorted() creates new list, original list stays unchanged
more flexible for lists, tuples, Strings
output is a list
'''


earth_metals = ["Berylium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
sorted_earth_mentals = sorted(earth_metals)
print(sorted_earth_mentals)
print(earth_metals)

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
sorted_data = sorted(data)
print(sorted_data)
print(data)

print(sorted("Alphabetical"))