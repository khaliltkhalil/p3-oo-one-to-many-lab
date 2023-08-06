class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise TypeError("Wrong Pet Type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(
            [pet for pet in Pet.all if pet.owner == self], key=lambda x: x.name
        )
