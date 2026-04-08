import random


class DataGenerator:

    @staticmethod
    def generate_pet_id():
        return random.randint(1000, 9999)