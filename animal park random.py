import random
import math

class Animal:
    def __init__(self, x, y, gender):
        self.x = x
        self.y = y
        self.gender = gender

    def move(self, move_range, grid_size):
        self.x = max(0, min(grid_size, self.x + random.randint(-move_range, move_range)))
        self.y = max(0, min(grid_size, self.y + random.randint(-move_range, move_range)))

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Sheep(Animal):
    MOVE_RANGE = 2

class Wolf(Animal):
    MOVE_RANGE = 3

class Cow(Animal):
    MOVE_RANGE = 2

class Chicken(Animal):
    MOVE_RANGE = 1

class Lion(Animal):
    MOVE_RANGE = 4

class Hunter(Animal):
    MOVE_RANGE = 1
class Environment:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def move_animals(self):
        for animal in self.animals:
            animal.move(animal.MOVE_RANGE, self.grid_size)

    def resolve_interactions(self):
        new_animals = []
        for i, animal in enumerate(self.animals):
            for other in self.animals[i+1:]:
                distance = animal.distance_to(other)
                #Hunting
                if isinstance(animal, Wolf) and distance <= 4 and isinstance(other, (Sheep, Chicken)):
                    self.animals.remove(other)
                elif isinstance(animal, Lion) and distance <= 5 and isinstance(other, (Sheep, Cow)):
                    self.animals.remove(other)
                elif isinstance(animal, Hunter) and distance <= 8 and isinstance(other, Animal):
                    self.animals.remove(other)
                # Reproduction
 
                elif type(animal) == type(other) and animal.gender != other.gender and distance <= 3:
                    new_animals.append(type(animal)(random.randint(0, self.grid_size), random.randint(0, self.grid_size), random.choice(['male', 'female'])))
        self.animals.extend(new_animals)
def simulate(environment, steps):
    for _ in range(steps):
        environment.move_animals()
        environment.resolve_interactions()
    
# Counting animals at the end of the simulation

    summary = {}
    for animal in environment.animals:
        species = type(animal).__name__
        summary[species] = summary.get(species, 0) + 1

    return summary
if __name__ == "__main__":
    grid_size = 500
    environment = Environment(grid_size)

# Adding initial animals

    for _ in range(15):
        environment.add_animal(Sheep(random.randint(0, grid_size), random.randint(0, grid_size), random.choice(['male', 'female'])))
    for _ in range(5):
        environment.add_animal(Wolf(random.randint(0, grid_size), random.randint(0, grid_size), random.choice(['male', 'female'])))
    for _ in range(5):
        environment.add_animal(Cow(random.randint(0, grid_size), random.randint(0, grid_size), random.choice(['male', 'female'])))
    for _ in range(10):
        environment.add_animal(Chicken(random.randint(0, grid_size), random.randint(0, grid_size), random.choice(['male', 'female'])))
    for _ in range(4):
        environment.add_animal(Lion(random.randint(0, grid_size), random.randint(0, grid_size), random.choice(['male', 'female'])))
    environment.add_animal(Hunter(random.randint(0, grid_size), random.randint(0, grid_size), 'male'))

# Running the simulation

    result = simulate(environment, 1000)
    print("final_result")
    for species, count in result.items():
        print(f"{species}: {count}")
