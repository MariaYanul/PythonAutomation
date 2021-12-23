class Zoo:
    def __init__(self, animal_type: str, animal_name: str, num_cage: int) -> None:
        self.animal_type = animal_type
        self.animal_name = animal_name
        self.num_cage = num_cage

if __name__ == "__main__":
    animal = Zoo('mammals', 'Grizly', 13)
    print(animal.animal_type)
    print(animal.animal_name)
    print(animal.num_cage)

