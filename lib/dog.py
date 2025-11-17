#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name="Fido", breed="Pug"):
    
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            self.name = None

        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self.breed = None

    
    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
            self.name = new_name
        else:
            print("Name must be string between 1 and 25 characters.")


    def set_breed(self, new_breed):
        if new_breed in APPROVED_BREEDS:
            self.breed = new_breed
        else:
            print("Breed must be in list of approved breeds.")