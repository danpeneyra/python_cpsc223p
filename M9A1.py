# Daniel Peneyra
# Student ID: 879117264
# Section: C22P-18254 07
# Assignment: Module 9 Assignment 1

population_dict = {
}

while True:
    city = input("What is the next city? (enter q to quit) "
    if city == 'q':
    	break
    population = input("What is the population of {city}")
    population_dict[city] = int(population)
    max_small_town = input("What is the largest population for a small town? ")

with open('populationdata.txt', 'w') as out_file:
	out_file.write("Big cities:\n")
    
    for city in population_dict:
        if population_dict[city] > max_small_town:
			out_file.write(f"{city},{population_dict[city]}\n")
    