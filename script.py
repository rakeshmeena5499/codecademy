destinations=['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler=['Erin Wilked', 'Shanghai, China', ['hitorical site', 'art']]

def get_destination_index(destination):
	destination_index=destinations.index(destination)
	return destination_index

#testing the function 

#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
	traveler_destination=traveler[1];
	traveler_destination_index=get_destination_index(traveler_destination)
	return traveler_destination_index

#testing the function

test_destination_index=get_traveler_location(test_traveler)

print(test_destination_index)


