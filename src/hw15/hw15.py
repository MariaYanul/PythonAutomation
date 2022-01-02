class Dog:
    def __init__(self, name: str, age: int, sex: str, weight: int):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__weight = weight

    def dog_name(self):
        print("The dog's name is ", self.__name)

    def dog_age(self):
        print("The dog's name is ", self.__age)

    def dog_sex(self):
        print("The dog's sex is ", self.__sex)

    def dog_weight(self):
        print("The dog's weight is ", self.__weight)

class Mustiff(Dog):

    def dog_info(self, breed: str, wool_length: str, mood: str):
        print(f"Breed : {breed}, the wool length: {wool_length}, dog's mood: {mood}")


if __name__ == "__main__":
    pes1 = Mustiff("Tyzik", 13, "M", 80)
    pes1.dog_name()
    pes1.dog_age()
    pes1.dog_sex()
    pes1.dog_weight()
    pes1.dog_info("English", "Not long", "Calm")
    print(50 * "-")
    pes2 = Mustiff("Tia", 5, "F", 40)
    pes2.dog_name()
    pes2.dog_age()
    pes2.dog_sex()
    pes2.dog_weight()
    pes2.dog_info("Tibetsk", "Long", "Calm")
